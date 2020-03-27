import os
import lines
import time
import datetime
import pymysql
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, Response

app = Flask(__name__, static_url_path="/assets")

DB = pymysql.connect("localhost", "root", "root", "interpolation")


@app.route("/calculate", methods=["GET"])
def core():
    return render_template("calculation.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    count = """
            SELECT COUNT(*) FROM plot_log WHERE create_time >= %s
        """
    cursor = DB.cursor()
    now = datetime.datetime.now()
    former_today = now - datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                            microseconds=now.microsecond)
    cursor.execute(count, (former_today.timestamp(), ))
    ans = cursor.fetchone()
    download_count_sql = """
            SELECT download_times FROM plot_log WHERE create_time >= %s
        """
    cursor.execute(download_count_sql, (former_today.timestamp(), ))
    count_list = cursor.fetchall()
    counts = 0
    if count_list is not None:
        for c in count_list:
            counts += c[0]
    cal_sql = """
            SELECT COUNT(*) FROM plot_log
        """
    cursor.execute(cal_sql)
    have_cal = cursor.fetchone()[0]
    cursor.close()
    if request.method == "POST":
        cursor = DB.cursor()
        try:
            generator = LineGenerator.get_by_line_type()
            md5 = generator.get_request_md5()
            sql = f"""
                SELECT file_name FROM plot_log WHERE plot_md5 = '{pymysql.escape_string(str(md5))}'
            """
            cursor.execute(sql)
            file_name = cursor.fetchone()
            if file_name is None:
                path, file_name = generator.generate()
                sql = f"""
                    INSERT INTO plot_log(host,plot_md5,file_name) VALUES ('{request.host}','{pymysql.escape_string(str(md5))}','{file_name}')
                """
                cursor.execute(sql)
                DB.commit()
                print(1)
            else:
                print(2)
                path = f"/assets/img/{file_name[0]}"
        except ValueError as e:
            import traceback
            print(traceback.format_exc())
            return str(e) or "错误的数据类型!"
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            return str(e)
        return render_template("index.html", **{"path": path}, count=ans[0], downloads_count=counts, hava_cal=have_cal, file_name=file_name[0])
    return render_template("index.html", path="/assets/img/8.png", count=ans[0], downloads_count=counts,
                           hava_cal=have_cal, file_name="8.png")


@app.route("/download/<file_name>")
def download(file_name):
    cursor = DB.cursor()
    sql = """
        SELECT * FROM plot_log WHERE file_name = %s
    """
    cursor.execute(sql, (pymysql.escape_string(file_name),))
    ans = cursor.fetchone()
    if ans is None:
        cursor.close()
        return "图片不存在!"
    with open(os.path.join(os.getcwd(), "static", "img", file_name), "rb") as f:
        resp = Response(mimetype="image/png", response=f.read())
        sql = """
            UPDATE plot_log SET download_times=download_times+1 WHERE file_name=%s
        """
        cursor.execute(sql, (file_name, ))
        DB.commit()
        cursor.close()
        return resp


class LineGenerator(object):
    def __init__(self, line_list):
        self._line_list = line_list

    def generate(self):
        for obj in self._line_list:
            obj.generate()
        f_name = f"calculated_{int(time.time())}.png"
        path = os.path.join(os.getcwd(), "static", "img", f_name)
        plt.savefig(path)
        plt.cla()
        return f"/assets/img/{f_name}", f_name

    @classmethod
    def get_by_line_type(cls):
        line_types = request.form.getlist("lineType")
        line_list = []
        for line in line_types:
            if line not in {"newton", "laGrange", "hermite"}:
                raise ValueError("错误的线段类型!")
        for line in line_types:
            obj = getattr(lines, line.capitalize())()
            obj.validate()
            line_list.append(obj)
        return cls(line_list)

    def get_request_md5(self):
        import hashlib
        md5 = hashlib.md5()
        for line in self._line_list:
            md5.update(str(line).encode("utf-8"))
        return md5.digest()


if __name__ == '__main__':
    app.run()
