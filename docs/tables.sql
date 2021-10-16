CREATE TABLE "faculty" (
	"faculty_id" CHAR(36) PRIMARY KEY,
	"faculty_name"	TEXT NOT NULL UNIQUE
);

CREATE TABLE "groups" (
	"groups_id" CHAR(36) PRIMARY KEY,
	"groups_name"	TEXT NOT NULL UNIQUE,
	"faculty_id"	CHAR(36) NOT NULL,
	FOREIGN KEY("faculty_id") REFERENCES "faculty"("faculty_id")
);

CREATE TABLE "student" (
	"student_id"	CHAR(36) PRIMARY KEY,
	"surname"	TEXT NOT NULL,
	"first_name"	TEXT NOT NULL,
	"middle_name"	TEXT DEFAULT NULL,
	"gender"	TEXT NOT NULL CHECK("gender" IN ('Мужской','Женский')),
	"birthdate"	BLOB NOT NULL,
	"groups_id"	CHAR(36) NOT NULL,
	FOREIGN KEY("groups_id") REFERENCES "groups"("groups_id")
);

CREATE TABLE "building" (
	"building_id"	CHAR(36) PRIMARY KEY,
	"building_address" TEXT NOT NULL UNIQUE
);

CREATE TABLE "commandant" (
	    "commandant_id"	CHAR(36) PRIMARY KEY,
	    "surname"	TEXT NOT NULL,
	    "first_name"	TEXT NOT NULL,
	    "middle_name"	TEXT NOT NULL,
	    "building_id"	CHAR(36) NOT NULL,
	    FOREIGN KEY("building_id") REFERENCES "building"("building_id")
);

CREATE TABLE "section" (
	"section_id"	CHAR(36) PRIMARY KEY,
	"section_number"	INTEGER NOT NULL,
	"free_rooms"	INTEGER NOT NULL,
	"building_id"	CHAR(36) NOT NULL,
	FOREIGN KEY("building_id") REFERENCES "building"("building_id")
);

CREATE TABLE "room" (
	"room_id"	CHAR(36) PRIMARY KEY,
	"room_number"	INTEGER NOT NULL,
	"total_beds"	INTEGER NOT NULL,
	"free_of_beds"	INTEGER NOT NULL,
	"section_id"	CHAR(36) NOT NULL,
	FOREIGN KEY("section_id") REFERENCES "section"("section_id")
);

CREATE TABLE "lodgers" (
	"lodgers_id"	CHAR(36) PRIMARY KEY,
	"check_in_date"	TEXT NOT NULL,
	"eviction_date"	TEXT DEFAULT NULL,
	"room_id"	CHAR(36) NOT NULL,
	"student_id"	CHAR(36) NOT NULL,
	FOREIGN KEY("room_id") REFERENCES "room"("room_id"),
	FOREIGN KEY("student_id") REFERENCES "student"("student_id")
);
