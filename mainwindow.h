/*************************************************************************\
  * KClient - A Toy Client in Qt
  *
  * Author : Manohar Kuse (mpkuse@ust.hk)
  * Date   : 26th Mar, 2014
  * Webpage : http://kusemanohar.wordpress.com/2014/03/26/qt-network-programming/
\*************************************************************************/




#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTcpSocket>
#include <QAbstractSocket>
#include <QHostAddress>
#include <QMessageBox>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    

private slots:
    // This function is called whenever, we click the send button in the UI
    void on_sendButton_clicked();

    // This function is called whenever we want to turn LED on
    void on_pushButton_clicked();

    // This function is called whenever we want to turn LED off
    void on_pushButton_2_clicked();

    // This function is called when you click the "connect" button in the ui (user-interface)
    void on_connectButton_clicked();

    // This function is called when the connection has been established successfully with the server stated.
    void connectionInit();

    // This function is called if there is an error (or disruption) in the connection
    void handleError(QAbstractSocket::SocketError err);

    // This function is called when the data is fully arrived from the server to the client
    void dataArrived();

private:
    Ui::MainWindow *ui;

    // Variable (socket) to hold the client connection data
    QTcpSocket tcpSocket;
};

#endif // MAINWINDOW_H
