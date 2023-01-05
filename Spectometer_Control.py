import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import OceanDirect as od


class SpectrometerControlWindow(QMainWindow):
    """Spectrometer Control Window
        GUI window with a line edit for the user to input an exposure time in milliseconds, 
        and a button to set the exposure time on the spectrometer
        Parameters:
            QMainWindow (PyQt5.QtWidgets.QMainWindow): Inherits from QMainWindow

        Attributes:
            exposureLabel (PyQt5.QtWidgets.QLabel): Label for the exposure time line edit
            exposureEdit (PyQt5.QtWidgets.QLineEdit): Line edit for the exposure time
            setExposureButton (PyQt5.QtWidgets.QPushButton): Button to set the exposure time
            spec (OceanDirect.Spectrometer): Spectrometer object
            """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Spectrometer Control')
        self.setGeometry(300, 300, 300, 150)

        # Create widgets
        self.exposureLabel = QLabel('Exposure Time (ms)', self)
        self.exposureEdit = QLineEdit(self)
        self.setExposureButton = QPushButton('Set Exposure', self)
        self.setExposureButton.clicked.connect(self.setExposure)

        # Set widget layout
        self.exposureLabel.move(20, 20)
        self.exposureEdit.move(150, 20)
        self.setExposureButton.move(20, 50)

        # Initialize spectrometer
        self.spec = od.Spectrometer()
        self.spec.init()

    def setExposure(self):
        exposure = int(self.exposureEdit.text())
        self.spec.setIntegrationTime(exposure)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpectrometerControlWindow()
    window.show()
    sys.exit(app.exec_())
