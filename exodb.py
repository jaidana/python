import sqlite3

def afficher(m):
    print(m)
    curseur.execute("""
        SELECT * FROM user_t
        """)
    rows = curseur.fetchall()
    for r in rows:
            print(r)

#creer la base de donnéees
connection= sqlite3.connect('base.db')
curseur = connection.cursor()

#créer la table
curseur.execute("""
     CREATE TABLE IF NOT EXISTS user_t (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name_f TEXT UNIQUE,
         room_f INTEGER
         )
""")

# inserer des données: Riri, 10
curseur.execute("""
    INSERT INTO
        user_t(name_f, room_f)
    values (?,?)""", ("Riri",10)
)

afficher("On a inséré Riri ")


#faire une list
liusers= [('fifi',10),('loulou', 11)]
curseur.executemany("""
    INSERT INTO
        user_t(name_f, room_f)
    VALUES (?,?)

""",liusers)
afficher("AFFICHER à nouveau le contenu de la table")
print("j'insère RIRI plusieurs fois")            
try:
    curseur.execute("""
    INSERT INTO
        user_t(name_f, room_f)
    values (?,?)""", ("Riri",10)
)     
except sqlite3.IntegrityError:
    print('le nom exsite déja')
    
curseur.execute("""
  INSERT INTO
      user_t(name_f, room_f)
  VALUES (?,?)
""",('Riri',20))
afficher('Aprés plusieurs insertions de Riri')
  

