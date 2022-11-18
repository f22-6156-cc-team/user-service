from flask import Flask, Response, request
import json
from models.User import UserQueryModel
from models.PersonalPreference import PersonalPreferenceQueryModel
from models.RoommateRequirement import RoommateRequirementQueryModel
from flask_cors import CORS


# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/api/users", methods=["GET"])
def get_all_users():
    try:
        with UserQueryModel() as uqm:
            users = uqm.get_all_users()
            users_json = serialize(users, "User")
            if users_json:
                rsp = Response(json.dumps(users_json), status=200, content_type="application.json")
            else:
                rsp = Response("Users Not Found", status=404, content_type="text/plain")
            return rsp
    except Exception as e:
        print(str(e))
        rsp = Response("Internal Server Error: " + str(e), status=500, content_type="text/plain")
        return rsp


@app.route("/api/user/<uid>", methods=["GET", "POST", "PUT", "DELETE"])
def user_by_user_id(uid):
    def get_user_by_user_id(uid):
        return UserQueryModel().get_user_by_user_id(uid)

    try:
        with UserQueryModel() as uqm:
            if request.method == "GET":
                try:
                    user = uqm.get_user_by_user_id(uid)
                    user_json = serialize(user, "User")
                    if user_json:
                        rsp = Response(json.dumps(user_json), status=200, content_type="application.json")
                    else:
                        rsp = Response("User Not Found", status=404, content_type="text/plain")
                    return rsp
                except Exception as e:
                    rsp = Response("User Not Found", status=404, content_type="text/plain")
                    return rsp
            elif request.method == "POST":
                user_info = request.get_json()
                if get_user_by_user_id(uid):
                    rsp = Response("User with user_id {} has already existed".format(uid),
                                   status=409, content_type="text/plain")
                    return rsp
                else:
                    uqm.add_user_by_user_id(user_id=uid, user_info=user_info)
                    created_user = get_user_by_user_id(uid)
                    created_user_json = serialize(created_user, "User")
                    rsp = Response(json.dumps(created_user_json), status=200, content_type="application.json")
                    return rsp
            elif request.method == "PUT":
                user_info = request.get_json()
                if get_user_by_user_id(uid):
                    uqm.update_user_by_user_id(user_id=uid, user_info=user_info)
                    updated_user = get_user_by_user_id(uid)
                    updated_user_json = serialize(updated_user, "User")
                    rsp = Response(json.dumps(updated_user_json), status=200, content_type="application.json")
                    return rsp
                else:
                    rsp = Response("User Not Found", status=404, content_type="text/plain")
                    return rsp
            elif request.method == "DELETE":
                delete_user = get_user_by_user_id(uid)
                if delete_user:
                    uqm.delete_user_by_user_id(uid)
                    rsp = Response("User with user_id {} is successfully deleted.".format(uid), status=200,
                                   content_type="application/json")
                else:
                    rsp = Response("User with user_id {} not found".format(uid), status=404,
                                   content_type="text/plain")
                return rsp
    except Exception as e:
        print(str(e))
        rsp = Response("Internal Server Error: " + str(e), status=500, content_type="text/plain")
        return rsp


@app.route("/api/user/<uid>/personal_preference", methods=["GET", "POST", "PUT"])
def personal_preference_by_user_id(uid):
    try:
        try:
            user = UserQueryModel().get_user_by_user_id(uid)
            if user:
                with PersonalPreferenceQueryModel() as ppqm:
                    if request.method == "GET":
                        personal_preference = ppqm.get_personal_preference_by_user_id(uid)
                        personal_preference_json = serialize(personal_preference, "PersonalPreference")
                        if personal_preference_json:
                            rsp = Response(json.dumps(personal_preference_json), status=200,
                                           content_type="application.json")
                        else:
                            rsp = Response("Personal Preference Not Found", status=404, content_type="text/plain")
                        return rsp
                    elif request.method == "POST":
                        personal_preference_info = request.get_json()
                        if user.personalPreferenceId is None:
                            ppqm.add_personal_preference_by_user_id(uid, personal_preference_info)
                            created_personal_preference = ppqm.get_personal_preference_by_user_id(uid)
                            update_user = {"personalPreferenceId": created_personal_preference.personalPreferenceId}
                            UserQueryModel().update_user_by_user_id(uid, update_user)
                            created_personal_preference_json = serialize(created_personal_preference,
                                                                         "PersonalPreference")
                            rsp = Response(json.dumps(created_personal_preference_json), status=200,
                                           content_type="application.json")
                            return rsp
                        else:
                            existing_id = user.personalPreferenceId
                            rsp = Response("User has already had personal preference with id {}".format(existing_id),
                                           status=409, content_type="text/plain")
                            return rsp
                    elif request.method == "PUT":
                        personal_preference_info = request.get_json()
                        if user.personalPreferenceId is not None:
                            ppqm.update_personal_preference_by_user_id(uid, personal_preference_info)
                            updated_personal_preference = ppqm.get_personal_preference_by_user_id(uid)
                            updated_personal_preference_json = serialize(updated_personal_preference, "PersonalPreference")
                            rsp = Response(json.dumps(updated_personal_preference_json), status=200,
                                           content_type="application.json")
                            return rsp
                        else:
                            rsp = Response("Personal Preference Not Found", status=404, content_type="text/plain")
                            return rsp
            else:
                rsp = Response("User Not Found", status=404, content_type="text/plain")
                return rsp
        except Exception as e:
            rsp = Response("User Not Found", status=404, content_type="text/plain")
            return rsp
    except Exception as e:
        print(str(e))
        rsp = Response("Internal Server Error: " + str(e), status=500, content_type="text/plain")
        return rsp


@app.route("/api/user/<uid>/roommate_requirement", methods=["GET", "POST", "PUT"])
def roommate_requirement_by_user_id(uid):
    try:
        try:
            user = UserQueryModel().get_user_by_user_id(uid)
            if user:
                with RoommateRequirementQueryModel() as rrqm:
                    if request.method == "GET":
                        roommate_requirement = rrqm.get_roommate_requirement_by_user_id(uid)
                        roommate_requirement_json = serialize(roommate_requirement, "RoommateRequirement")
                        if roommate_requirement_json:
                            rsp = Response(json.dumps(roommate_requirement_json), status=200,
                                           content_type="application.json")
                        else:
                            rsp = Response("Roommate Requirement Not Found", status=404, content_type="text/plain")
                        return rsp
                    elif request.method == "POST":
                        roommate_requirement_info = request.get_json()
                        if user.roommateRequirementId is None:
                            rrqm.add_roommate_requirement_by_user_id(uid, roommate_requirement_info)
                            created_roommate_requirement = rrqm.get_roommate_requirement_by_user_id(uid)
                            update_user = {"roommateRequirementId": created_roommate_requirement.roommateRequirementId}
                            UserQueryModel().update_user_by_user_id(uid, update_user)
                            created_roommate_requirement_json = serialize(created_roommate_requirement,
                                                                          "RoommateRequirement")
                            rsp = Response(json.dumps(created_roommate_requirement_json), status=200,
                                           content_type="application.json")
                            return rsp
                        else:
                            existing_id = user.roommateRequirementId
                            rsp = Response("User has already had roommate requirement with id {}".format(existing_id),
                                           status=409, content_type="text/plain")
                            return rsp
                    elif request.method == "PUT":
                        roommate_requirement_info = request.get_json()
                        if user.roommateRequirementId is not None:
                            rrqm.update_roommate_requirement_by_user_id(uid, roommate_requirement_info)
                            updated_roommate_requirement = rrqm.get_roommate_requirement_by_user_id(uid)
                            updated_roommate_requirement_json = serialize(updated_roommate_requirement,
                                                                          "RoommateRequirement")
                            rsp = Response(json.dumps(updated_roommate_requirement_json), status=200,
                                           content_type="application.json")
                            return rsp
                        else:
                            rsp = Response("Roommate Requirement Not Found", status=404, content_type="text/plain")
                            return rsp
            else:
                rsp = Response("User Not Found", status=404, content_type="text/plain")
                return rsp
        except Exception as e:
            rsp = Response("User Not Found", status=404, content_type="text/plain")
            return rsp
    except Exception as e:
        print(str(e))
        rsp = Response("Internal Server Error: " + str(e), status=500, content_type="text/plain")
        return rsp


def serialize(model_object, model_type):
    result = []
    if not isinstance(model_object, list):
        model_object = [model_object]
    for obj in model_object:
        if model_type == "User":
            record = {
                "userId": obj.userId,
                "isActive": obj.isActive,
                "isAdmin": obj.isAdmin,
                "username": obj.username,
                "firstName": obj.firstName,
                "lastName": obj.lastName,
                "personalPreferenceId": obj.personalPreferenceId,
                "roommateRequirementId": obj.roommateRequirementId
            }
        elif model_type == "PersonalPreference":
            record = {
                "userId": obj.userId,
                "personalPreferenceId": obj.personalPreferenceId,
                "gender": obj.gender,
                "sleepingTime": obj.sleepingTime,
                "wakeupTime": obj.wakeupTime,
                "cookingFrequency": obj.cookingFrequency,
                "cleaningFrequency": obj.cleaningFrequency,
                "isPetFriendly": obj.isPetFriendly,
                "isSmokingFriendly": obj.isSmokingFriendly,
                "isPartyFriendly": obj.isPartyFriendly,
                "isGuestWelcome": obj.isGuestWelcome
            }
        elif model_type == "RoommateRequirement":
            record = {
                "userId": obj.userId,
                "roommateRequirementId": obj.roommateRequirementId,
                "gender": obj.gender,
                "sleepingTime": obj.sleepingTime,
                "wakeupTime": obj.wakeupTime,
                "cookingFrequency": obj.cookingFrequency,
                "cleaningFrequency": obj.cleaningFrequency,
                "isPetFriendly": obj.isPetFriendly,
                "isSmokingFriendly": obj.isSmokingFriendly,
                "isPartyFriendly": obj.isPartyFriendly,
                "isGuestWelcome": obj.isGuestWelcome
            }
        result.append(record)
    if len(result) == 1:
        result = result[0]
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
