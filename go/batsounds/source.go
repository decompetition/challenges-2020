package main

import (
  "io"
  "log"
  "net"
  "time"
)

func echo(conn net.Conn) {
  // When everything else is done, close the connection
  defer conn.Close()

  b := make([]byte, 20)

  for {
    // Receive data via conn.Read into a buffer
    size, err := conn.Read(b[0:])
    if err == io.EOF {
      log.Println("Client disconnected")
      break
    }
    log.Printf("Received %d bytes: %s", size, string(b[0:size]))

    log.Printf("Writing %d bytes of data", size)
    if _, err := conn.Write(b[0:size]); err != nil {
      log.Println("Unable to write data")
      break
    }
  }
}

func main() {
  // Bind to TCP port 20080 on all interfaces
  listener, err := net.Listen("tcp", ":20080")
  if err != nil {
    log.Fatalln("Unable to bind to port")
  }

  tcplistener := listener.(*net.TCPListener)
  tcplistener.SetDeadline(time.Now().Add(time.Millisecond * 100))
  log.Println("Listening on 0.0.0.0:20080")

  // wait for connection, create net.Conn on connection established
  conn, err := listener.Accept()
  log.Println("Received connection...")
  if err != nil {
    log.Fatalln("Unable to accept connection")
  }

  // Handle the connection
  echo(conn)
}
