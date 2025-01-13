from django.db import models, connection
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Food(models.Model):
    PAGE_SIZE = 20

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    food_name = models.TextField()

    @staticmethod
    def search_food(keyword: str, page_number: int):
        offset = page_number * Food.PAGE_SIZE

        with connection.cursor() as cursor:
            #cursor.execute("SELECT pg_backend_pid()")
            #pid = cursor.fetchone()[0]
            #print("Connection PID:", pid)
            # Get only the records for current page
            params = [keyword, Food.PAGE_SIZE, offset]
            sql = """SELECT * FROM food_food WHERE food_name &@ %s
             ORDER BY id DESC LIMIT %s OFFSET %s
            """
            print("SQL:", cursor.mogrify(sql, params))

            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
