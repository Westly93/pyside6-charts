from ui_charts import Ui_MainWindow
from PySide6.QtGui import QIcon, Qt
from PySide6 import QtCharts
from PySide6.QtWidgets import QMainWindow


class ChartyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(':/icons/logo.png'))
        self.setWindowTitle("Charty App")

        self.piechart_btn.clicked.connect(self.switch_to_piechart)
        self.barchart_btn.clicked.connect(self.switch_to_barchart)
        self.linegraph_btn.clicked.connect(self.switch_to_linegraph)
        self.pushButton.clicked.connect(self.update_piechart)
        self.update_piechart()
        self.update_linegraph()
        self.update_barchart()
    # switch to different pages

    def switch_to_piechart(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_linegraph(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_barchart(self):
        self.stackedWidget.setCurrentIndex(2)

    # update piechart
    def update_piechart(self):
        self.pie_chart = QtCharts.QChart()
        self.pie_series = QtCharts.QPieSeries()
        self.pie_series.setLabelsVisible(True)
        self.pie_series.setLabelsPosition(QtCharts.QPieSlice.LabelOutside)

        self.python_slice = QtCharts.QPieSlice("Python", 0)
        self.javascript_slice = QtCharts.QPieSlice("Javascript", 0)
        self.java_slice = QtCharts.QPieSlice("Java", 0)
        self.csharp_slice = QtCharts.QPieSlice("C#", 0)
        self.pie_series.append(self.python_slice)
        self.pie_series.append(self.javascript_slice)
        self.pie_series.append(self.java_slice)
        self.pie_series.append(self.csharp_slice)
        self.pie_chart.addSeries(self.pie_series)
        self.pie_chart.setTitle("The Most Popular Programming languages")
        self.pie_chart.legend().setVisible(True)
        self.pie_chart.legend().setAlignment(Qt.AlignBottom)
        self.piechart_view.setChart(self.pie_chart)

        try:
            num_python = int(self.python.text())
            num_javascript = int(self.javascript.text())
            num_java = int(self.java.text())
            num_csharp = int(self.csharp.text())

            total = num_python + num_javascript + num_java + num_csharp
            if total > 0:
                self.python_slice.setValue(num_python/total * 100)
                self.javascript_slice.setValue(num_javascript/total * 100)
                self.java_slice.setValue(num_java/total * 100)
                self.csharp_slice.setValue(num_csharp/total * 100)
        except ValueError:
            pass

    def update_linegraph(self):
        chart = QtCharts.QChart()
        chart.setTitle("Popularity of programming languages over the years")
        years = ['2020', '2021', '2022', '2023', '2024']

        python_data = [10, 20, 30, 40, 50]
        javascript_data = [1, 2, 3, 4, 5]
        java_data = [3, 9, 10, 23, 40]
        csharp_data = [3, 3, 4, 8, 11]

        python_series = QtCharts.QLineSeries()
        python_series.setName("Python")
        for i in range(len(years)):
            python_series.append(i, python_data[i])
        chart.addSeries(python_series)

        javascript_series = QtCharts.QLineSeries()
        javascript_series.setName("Javascript")
        for i in range(len(years)):
            javascript_series.append(i, javascript_data[i])
        chart.addSeries(javascript_series)

        java_series = QtCharts.QLineSeries()
        java_series.setName("Java")
        for i in range(len(years)):
            java_series.append(i, java_data[i])
        chart.addSeries(java_series)

        csharp_series = QtCharts.QLineSeries()
        csharp_series.setName("C#")
        for i in range(len(years)):
            csharp_series.append(i, csharp_data[i])
        chart.addSeries(csharp_series)

        x_axis = QtCharts.QBarCategoryAxis()
        x_axis.append(years)
        chart.addAxis(x_axis, Qt.AlignBottom)

        y_axis = QtCharts.QValueAxis()

        min_y = min(min(python_data), min(javascript_data),
                    min(java_data), min(csharp_data))
        max_y = max(max(python_data), max(javascript_data),
                    max(java_data), max(csharp_data))

        y_axis.setRange(min_y, max_y)
        chart.addAxis(y_axis, Qt.AlignLeft)

        python_series.attachAxis(x_axis)
        python_series.attachAxis(y_axis)

        javascript_series.attachAxis(x_axis)
        javascript_series.attachAxis(y_axis)

        java_series.attachAxis(x_axis)
        java_series.attachAxis(y_axis)

        csharp_series.attachAxis(x_axis)
        csharp_series.attachAxis(y_axis)
        self.linegraph_view.setChart(chart)

    def update_barchart(self):
        series = QtCharts.QBarSeries()
        series.setName("Programming Language Popularity over time")
        years = ['2020', '2021', '2022', '2023', '2024']

        python_data = [10, 20, 30, 40, 50]
        javascript_data = [1, 2, 3, 4, 5]
        java_data = [3, 9, 10, 23, 40]
        csharp_data = [3, 3, 4, 8, 11]

        barset_python = QtCharts.QBarSet("Python")
        barset_javascript = QtCharts.QBarSet("Javascript")
        barset_java = QtCharts.QBarSet("Java")
        barset_csharp = QtCharts.QBarSet("C#")

        for i in range(len(years)):
            barset_python.append(python_data[i])
            barset_javascript.append(javascript_data[i])
            barset_java.append(java_data[i])
            barset_csharp.append(csharp_data[i])
        series.append(barset_python)
        series.append(barset_csharp)
        series.append(barset_java)
        series.append(barset_javascript)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Programming Language popularity over the years")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(years)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        chart.addAxis(axis_y, Qt.AlignLeft)

        series.attachAxis(axis_y)

        self.barchart_view.setChart(chart)
