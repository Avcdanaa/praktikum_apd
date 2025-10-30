from json import load
from turtle import clear, delay
import func 

def main():
    while  True:
        load()
        mood=input('\Bagaimana Mood Kalian Hari ini?(Ketik 0 jika ingin dikeluar)')
        print(mood)
        delay()
        clear()
        if mood =='0':
            return False
        
if __name__ == "__main__":
    main()
