from models.BaseModel import BaseQueryModel, Base


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'autoload': True}


class UserQueryModel(BaseQueryModel):

    def get_all_users(self):
        return self.session.query(User).filter(User.isActive == True).all()

    def get_user_by_user_id(self, user_id):
        user = self.session.query(User).filter(User.userId == user_id).filter(User.isActive == True).first()
        return user

    def add_user_by_user_id(self, user_id, user_info=None):
        inactive_user = self.session.query(User).filter(User.userId == user_id).filter(User.isActive == False).first()
        if inactive_user:
            inactive_user.isActive = True
            if user_info:
                for key, value in user_info.items():
                    setattr(inactive_user, key, value)
            self.session.commit()
        else:
            user = User(userId=user_id, isActive=True)
            if user_info:
                for key, value in user_info.items():
                    setattr(user, key, value)
            self.session.add(user)
            self.session.commit()

    def update_user_by_user_id(self, user_id, user_info=None):
        user = self.session.query(User).filter(User.userId == user_id).filter(User.isActive == True).first()
        if user_info:
            for key, value in user_info.items():
                setattr(user, key, value)
        self.session.commit()

    def delete_user_by_user_id(self, user_id):
        user = self.session.query(User).filter(User.userId == user_id).filter(User.isActive == True).first()
        user.isActive = False
        self.session.commit()

