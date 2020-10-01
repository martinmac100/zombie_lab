from db.run_sql import run_sql
from models.biting import Biting

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        biting = Biting(result["human"], result["zombie"])
        bitings.append(biting)
    return bitings

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values) [0]
    biting = Biting(result["human"], result["id"])
    return biting

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)