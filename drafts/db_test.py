import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    ''' Create connectiond to a SQLite dataqbase '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    ''' Create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE sql statement
    '''

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:

        print(e)

def create_project(conn, project):
    ''' Create a new project into the projects table
        :param conn:
        :param project:
        :return: project_id
    '''
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?)
          '''
    c = conn.cursor()
    c.execute(sql,project)
    print('Project created')
    return c.lastrowid

def create_task(conn, task):
    ''' Create a new task in the tasks table
        :param conn:
        :param task:
        :return: task_id
    '''
    sql = ''' INSERT INTO tasks(name,priority,status_id, project_id,
              begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''

    c = conn.cursor()
    c.execute(sql, task)
    print('Task created')
    return c.lastrowid

def update_task(conn, task):
    ''' Update priority,begin date and end date of a task
    :param conn:
    :param task:
    :return: project id
    '''

    sql = '''UPDATE tasks
             SET priority = ?,
                 begin_date = ?,
                 end_date = ?
             WHERE id = ?'''
    c = conn.cursor()
    c.execute(sql,task)
    conn.commit()

def delete_task(conn, id):
    ''' Delete selected task'
        :param conn:
        :param id:
        :return:
    '''

    sql = 'DELETE FROM tasks WHERE id = ?'

    c=conn.cursor()
    c.execute(sql, (id,))
    conn.commit()

def select_all_tasks(conn):
    ''' Query all rows in the tasks table:
        :param conn: connection object
        :return:
    '''
    sql = 'SELECT * FROM tasks'

    c= conn.cursor()
    c.execute(sql)
    rows = c.fetchall()

    for row in rows:
        print(row)

def select_task(conn, id):
    ''' Query all task with same project_id from tasks
        :param conn:
        :param id: project_id
    '''
    sql = 'SELECT * FROM tasks WHERE project_id = ?'

    c= conn.cursor()
    c.execute(sql, (id,))
    rows = c.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"test_database.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                        ); """

    sql_create_task_table =     ''' CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,

                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                        ); '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_task_table)

    else:
        print("Error! Cannot create the database connection")

    with conn:
        project = ('NOT Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn,project)

        task_1 = ('Analyze the requirements of the app', 1, 1, project_id,
                   '2015-01-01','2015-01-05')
        task_2 = ('Confirm with user about top requirements', 1, 1, project_id,
                   '2015-01-03', '2015-01-05')

        create_task(conn, task_1)
        create_task(conn, task_2)

        # update_task(conn,(2,'000','000',2))
        # delete_task(conn,14)

    select_all_tasks(conn)



if __name__ == '__main__':
    main()
    prit('succes')


