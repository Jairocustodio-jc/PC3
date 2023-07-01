import pymysql

class DAOAlumno:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", db="PC3")

    def read(self, id=None):
        con = DAOAlumno.connect(self)
        cursor = con.cursor()

        try:
            if id is None:
                cursor.execute("SELECT * FROM alumnos ORDER BY nombre ASC")
            else:
                cursor.execute("SELECT * FROM alumnos WHERE username = %s ORDER BY nombre ASC", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = DAOAlumno.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO alumnos(username, nombre, apellidos, clave) VALUES (%s, %s, %s, %s)",
                           (data['username'], data['nombre'], data['apellidos'], data['clave'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOAlumno.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE alumnos SET nombre = %s, apellidos = %s, clave = %s WHERE username = %s",
                           (data['nombre'], data['apellidos'], data['clave'], id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOAlumno.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM alumnos WHERE username = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
