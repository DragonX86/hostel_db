CREATE TRIGGER facultyGenerateGUID
AFTER INSERT ON faculty
FOR EACH ROW
WHEN (NEW.faculty_id IS NULL)
BEGIN
   UPDATE faculty SET faculty_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER groupsGenerateGUID
AFTER INSERT ON groups
FOR EACH ROW
WHEN (NEW.groups_id IS NULL)
BEGIN
   UPDATE groups SET groups_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER studentGenerateGUID
AFTER INSERT ON student
FOR EACH ROW
WHEN (NEW.student_id IS NULL)
BEGIN
   UPDATE student SET student_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER buildingGenerateGUID
AFTER INSERT ON building
FOR EACH ROW
WHEN (NEW.building_id IS NULL)
BEGIN
   UPDATE building SET building_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER commandantGenerateGUID
AFTER INSERT ON commandant
FOR EACH ROW
WHEN (NEW.commandant_id IS NULL)
BEGIN
   UPDATE commandant SET commandant_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER sectionGenerateGUID
AFTER INSERT ON section
FOR EACH ROW
WHEN (NEW.section_id IS NULL)
BEGIN
   UPDATE section SET section_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER roomGenerateGUID
AFTER INSERT ON room
FOR EACH ROW
WHEN (NEW.room_id IS NULL)
BEGIN
   UPDATE room SET room_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;

CREATE TRIGGER lodgersGenerateGUID
AFTER INSERT ON lodgers
FOR EACH ROW
WHEN (NEW.lodgers_id IS NULL)
BEGIN
   UPDATE lodgers SET lodgers_id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))) WHERE rowid = NEW.rowid;
END;
