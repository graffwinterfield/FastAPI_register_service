import datetime
import time

from models import Note
from sqlalchemy.orm import Session
from fastapi import Depends, status, APIRouter, Query, Body, HTTPException
from database import get_db
from functions import Mail, save_to_db

mail = Mail()
router = APIRouter()
MAX_NOTIFICATIONS = 100
server = mail.connect_to_mail()


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_note(db: Session = Depends(get_db), user_id: str = Query(...), target_id: str = Query(...),
                key: str = Query(...), data: dict = Body(None)):
    global server
    success = mail.check_conn(server=server)
    while success is not True:
        server = mail.connect_to_mail()
        success = mail.check_conn(server=server)
        time.sleep(2)
    user_notifications = db.query(Note).filter(Note.user_id == user_id).all()
    if len(user_notifications) >= MAX_NOTIFICATIONS:
        raise HTTPException(status_code=400, detail="Max number of notifications reached")

    timestamp = datetime.datetime.utcnow().timestamp()
    is_new = True
    new_note = Note(timestamp=timestamp, is_new=is_new, user_id=user_id, target_id=target_id,
                    key=key, data=data)
    keys = {
        "- registration": "(Только отправит пользователю Email)",
        "- new_message": "(только создаст запись в документе пользователя)",
        "- new_post": "(только создаст запись в документе пользователя)",
        "- new_login": "(Создаст запись в документе пользователя и отправит email)"
    }
    if key == 'registration':
        mail.send_email(server=server, text=key)
    elif key == 'new_message':
        save_to_db(new_note, db)
    elif key == 'new_post':
        save_to_db(new_note, db)
    elif key == 'new_login':
        save_to_db(new_note, db)
        mail.send_email(server=server, text=key)
    else:
        return {"success": False, "KeyError": keys}
    return {"success": True, "list": new_note}


@router.get('/list', status_code=status.HTTP_200_OK)
def info(db: Session = Depends(get_db), user_id: str = Query(...), skip: int = Query(0), limit: int = Query(10)):
    user_notifications = None
    new = None
    try:
        user_notifications = db.query(Note).filter(Note.user_id == user_id).offset(skip).limit(limit).all()
        new = db.query(Note).filter(Note.user_id == user_id, Note.is_new == True).offset(skip).limit(limit).all()
    except Exception as e:
        print(e)
    return {
        "success": "true",
        "data": {
            "elements": len(user_notifications),
            "new": len(new),
            "request": {"user_id": user_id,
                        "skip": skip,
                        "limit": limit},
            "list": user_notifications
        }
    }


@router.post('/read', status_code=status.HTTP_200_OK)
def read(db: Session = Depends(get_db), user_id: str = Query(...), notification_id: int = Query(...)):
    notification = db.query(Note).filter(Note.user_id == user_id, Note.id == notification_id).first()
    if notification:
        notification.is_new = False
        db.commit()
        return {"success": True}
    else:
        return {"success": False}
