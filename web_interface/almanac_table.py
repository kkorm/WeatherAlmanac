from weather_api import monthly_record

class almanac_table:
    """
    Contains monthly data for a particular month and location for html output.
    
    Basic usage:
    >>> table = almanac_table(office, station, year, month)
    >>> table.load_month(office, station, year, month)
    >>> string = table.get_html_string()
    """
    def __init__(self, office, station, year, month):
        self.load_month(office, station, year, month)

    def load_month(self, office, station, year, month):
        """
        Loads new monthly data.

        :param site: NWS Office.
        :param station: NWS Station.
        :param year: Year of interest.
        :param month: Month of interest.
        """

        record = monthly_record.record(office, station, year, month)
        self.arr = record.get_month()

    def get_html_string(self):
        """Returns html string for monthly data."""

        if self.arr == ["invalid input"]:
            return "<p>Invalid input format</p>"
        else:
            rows_arr = len(self.arr)
            
            string_arr = []
            string_arr.append("<table><tr>")
            for row in range(0, 1):
                cols_arr = len(self.arr[row])
                for col in range(0, cols_arr):
                    string_arr.append("<th>" + self.arr[row][col] + "</th>")
                string_arr.append("</tr>")
                
            for row in range(1, rows_arr):
                cols_arr = len(self.arr[row])
                for col in range(0, cols_arr):
                    string_arr.append("<td>" + self.arr[row][col] + "</td>")
                string_arr.append("</tr>")
            string_arr.append("</tr></table>")
            
            string = "".join(string_arr)
            
            return string
