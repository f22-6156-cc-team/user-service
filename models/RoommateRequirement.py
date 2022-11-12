from models.BaseModel import BaseQueryModel, Base


class RoommateRequirement(Base):
    __tablename__ = 'RoommateRequirement'
    __table_args__ = {'autoload': True}


class RoommateRequirementQueryModel(BaseQueryModel):

    def get_roommate_requirement_by_user_id(self, user_id):
        roommate_requirement = self.session.query(RoommateRequirement)\
            .filter(RoommateRequirement.userId == user_id)\
            .first()
        return roommate_requirement

    def add_roommate_requirement_by_user_id(self, user_id, roommate_requirement_info=None):
        roommate_requirement = RoommateRequirement(userId=user_id)
        if roommate_requirement_info:
            for key, value in roommate_requirement_info.items():
                setattr(roommate_requirement, key, value)
        self.session.add(roommate_requirement)
        self.session.commit()

    def update_roommate_requirement_by_user_id(self, user_id, roommate_requirement_info=None):
        roommate_requirement = self.session.query(RoommateRequirement) \
            .filter(RoommateRequirement.userId == user_id) \
            .first()
        if roommate_requirement_info:
            for key, value in roommate_requirement_info.items():
                setattr(roommate_requirement, key, value)
        self.session.commit()