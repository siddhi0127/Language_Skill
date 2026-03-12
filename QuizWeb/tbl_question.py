import sqlite3
conn = sqlite3.connect("users.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblquestion(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain TEXT,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    answer TEXT
    ) """)
cursor.execute("""
INSERT INTO tblquestion(domain,question,option1,option2,option3,option4,answer)
VALUES
('aptitude','2 + 2 = ?','3','4','5','6','4'),
('aptitude','5 * 6 = ?','20','25','30','35','30'),
('python','Python is a ?','language','car','animal','game','language'),
('c','Who developed C?','Dennis Ritchie','James Gosling','Guido','Bjarne','Dennis Ritchie')
""")
conn.commit()
conn.close()

print("Question table created")