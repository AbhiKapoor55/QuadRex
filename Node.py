
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import QRex
import Repo
from Functions import Functions


class Node:

    def __init__(self, data: Functions):
        self.data = data
        self.next = None

