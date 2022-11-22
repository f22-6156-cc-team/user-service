drop database if exists user_service;
create database user_service;

drop table if exists user_service.User;
create table user_service.User
(
    userId                  varchar(256)   not null,
    isActive                boolean        not null,
    isAdmin                 boolean        not null,
    username                varchar(256)   not null,
    firstName               varchar(256)   not null,
    lastName                varchar(256)   not null,
    personalPreferenceId    int            null,
    roommateRequirementId   int            null,
    constraint User_pk
        primary key (userId)
);

drop table if exists user_service.PersonalPreference;
create table user_service.PersonalPreference
(
    userId                 varchar(256)                                        not null,
    personalPreferenceId   int                                                 not null  auto_increment,
    gender                 enum('Female', 'Male', 'Others')                    not null,
    sleepingTime           enum('before 10PM', '10PM to 12PM', 'after 12PM')   not null,
    wakeupTime             enum('before 7AM', '7AM to 9AM', 'after 9AM')       not null,
    cookingFrequency       enum('never', 'rarely', 'often', 'everyday')        not null,
    cleaningFrequency      enum('never', 'rarely', 'often', 'everyday')        not null,
    isPetFriendly          boolean                                             not null,
    isSmokingFriendly      boolean                                             not null,
    isPartyFriendly        boolean                                             not null,
    isGuestWelcome         boolean                                             not null,
    constraint PersonalPreference_pk
        primary key (personalPreferenceId),
    constraint PersonalPreference_User_fk
        foreign key (userId) references user_service.User (userId)
);

drop table if exists user_service.RoommateRequirement;
create table user_service.RoommateRequirement
(
    userId                  varchar(256)                                        not null,
    roommateRequirementId   int                                                 not null  auto_increment,
    gender                  enum('Female', 'Male', 'Others')                    not null,
    sleepingTime            enum('before 10PM', '10PM to 12PM', 'after 12PM')   not null,
    wakeupTime              enum('before 7AM', '7AM to 9AM', 'after 9AM')       not null,
    cookingFrequency        enum('never', 'rarely', 'often', 'everyday')        not null,
    cleaningFrequency       enum('never', 'rarely', 'often', 'everyday')        not null,
    isPetFriendly           boolean                                             not null,
    isSmokingFriendly       boolean                                             not null,
    isPartyFriendly         boolean                                             not null,
    isGuestWelcome          boolean                                             not null,
    constraint RoommateRequirement_pk
        primary key (roommateRequirementId),
    constraint RoommateRequirement_User_fk
        foreign key (userId) references user_service.User (userId)
);
