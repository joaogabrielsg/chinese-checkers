import pygame

from connection.client import Client


def main():
    client = Client('localhost', 65432)

    client.start_connection()

if __name__ == "__main__":
    main()
