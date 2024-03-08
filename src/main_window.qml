import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    visible: true
    width: Screen.width
    height: Screen.height
    color: "#404040"
    title: "Multimedia Editor v.0.1"

    Component.onCompleted: {
        showMaximized()
    }
}