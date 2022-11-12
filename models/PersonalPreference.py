from models.BaseModel import BaseQueryModel, Base


class PersonalPreference(Base):
    __tablename__ = 'PersonalPreference'
    __table_args__ = {'autoload': True}


class PersonalPreferenceQueryModel(BaseQueryModel):

    def get_personal_preference_by_user_id(self, user_id):
        personal_preference = self.session.query(PersonalPreference)\
            .filter(PersonalPreference.userId == user_id)\
            .first()
        return personal_preference

    def add_personal_preference_by_user_id(self, user_id, personal_preference_info=None):
        personal_preference = PersonalPreference(userId=user_id)
        if personal_preference_info:
            for key, value in personal_preference_info.items():
                setattr(personal_preference, key, value)
        self.session.add(personal_preference)
        self.session.commit()

    def update_personal_preference_by_user_id(self, user_id, personal_preference_info=None):
        personal_preference = self.session.query(PersonalPreference) \
            .filter(PersonalPreference.userId == user_id) \
            .first()
        if personal_preference_info:
            for key, value in personal_preference_info.items():
                setattr(personal_preference, key, value)
        self.session.commit()