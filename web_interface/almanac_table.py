from weather_api import monthly_record

class almanac_table:
    def __init__(self, office, station, year, month):
        self.load_month(office, station, year, month)

    def load_month(self, office, station, year, month):
        record = monthly_record.record(office, station, year, month)
        self.arr = record.get_month()

    def get_html_string(self):
        rows_arr = len(self.arr)
        cols_arr = len(self.arr[1])
        
        string_arr = []
        string_arr.append("<table><tr>")
        for row in range(0, rows_arr):
            for col in range(0, cols_arr):
                string_arr.append("<td>" + self.arr[row][col] + "</td>")
            string_arr.append("</tr>")
        string_arr.append("</tr></table>")
        
        #
        # ! Make more efficient?? !#
        #
        string = ""
        for each in string_arr:
            string += each
        
        return string