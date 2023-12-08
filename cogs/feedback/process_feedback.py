import nextcord
from sqlmodel import Session, select

from db.models import Feedback, User, Request


def process_feedback(interaction: nextcord.Interaction | None, message: nextcord.Message | None, session: Session, feedback: str, rating: int = 0) -> bool | None:
    if interaction:
        user_id = str(interaction.user.id)
    elif message:
        user_id = str(message.author.id)
    else:
        return None
    # query the database for the user who made the feedback
    statement = select(User).where(User.discord_id == user_id)
    db_user = session.exec(statement).first()
    if db_user is None:
        db_user = User(discord_id=user_id)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    request_id = None
    if message:
        # query the database for the request that the feedback is for
        statement = select(Request).where(
            Request.message_id == str(message.id))
        db_request = session.exec(statement).first()
        if db_request:
            request_id = db_request.id
    if request_id:
        # see if the user has rated this request
        statement = select(Feedback).where(
            Feedback.request_id == request_id).where(Feedback.user_id == db_user.id)
        db_feedback = session.exec(statement).first()
        if db_feedback:
            return False
    # create the feedback object
    feedback = Feedback(
        request_id=request_id,
        user_id=db_user.id,
        feedback=feedback,
        rating=rating
    )
    session.add(feedback)
    session.commit()
    return True
