#include <iostream>

using namespace std;

class Stack{
    private:
        int top;
        int arr[5];

    public:
        Stack ()
        {
            top = -1;
            for(int i = 0; i<5;i++)
            {
                arr[i] = 0;
            }
        }

        bool isEmpty()
        {
            if(top == -1)
                return true;
            else
                return false;
        }

        bool isFull()
        {
            if (top == 4)
                return true; //because top starts at -1 that's why 4 and not 5
            else
                return false;
        }

        void push(int val)
        {
            if(isFull())
            {
                cout<<"stack overflow"<<endl;
                return 0;
            }
            else
            {
                top++;
                arr[top] = val;
            }
        }

        int pop()
        {
            if(isEmpty())
            {
                cout<<"stack underflow"<<endl;
                return 0;

            }
            else
            {
                int popValue = arr[top];
                arr[top] = 0;
                top--;
                return popValue;
            }
        }


        int count()
        {
            return(top+1);
        }

        int peek(int pos)
        {
            if(isEmpty())
            {
                cout<<"stack underflow"<<endl;
                return 0;
            }
            else
            {
                return arr[pos];
            }
        }

        void change(int pos, int val)
        {
            arr[pos] = val;
            cout<<"value changed at location "<<pos<<endl;
        }

        void display()
        {
            cout<<"All values in the Stack are "<<endl;
            for(int i = 4;i>=0;i--)
            {
                cout<<arr[i]<<endl;
            }
        }
};

int main()
{
    Stack s1;
    int option, position, value;
    do
    {
        cout<<"What operation do you want to perform? Select Option number. Enter 0 to exit."<<endl;
        cout<<"1. Push()"<<endl;
        cout<<"2. Pop()"<<endl;
        cout<<"3. isEmpty()"<<endl;
        cout<<"4. isFull()"<<endl;
        cout<<"5. peek()"<<endl;
        cout<<"6. count()"<<endl;
        cout<<"7. change()"<<endl;
        cout<<"8. display()"<<endl;
        cout<<"9. Clear Screen"<<endl<<endl;

        cin>>option;
        switch(option)
        {
            case 0:
                break;
            case 1:
                cout<<"Enter an item to push in the stack"<<endl;
                cin>>value;
                s1.push(value);
                break;
            case 2:
                cout<<"Pop Function Called - Popped Value: "<<s1.pop()<<endl;
                break;
            case 3:
                if(s1.isEmpty())
                    cout<<"Stack is Empty"<<endl;
                else
                    cout<<"Stack is not Empty"<<endl;
                break;
            case 4:
                if(s1.isFull())
                    cout<<"Stack is Full"<<endl;
                else
                    cout<<"Stack is not Full"<<endl;
                break;
            case 5:
                cout<<"Enter position of item you want to peek: "<<endl;
                cin>>position;
                cout<<"Peek Function Called - Value at Position "<<position<<" is "<<s1.peek(position)<<endl;
                break;
            case 6:
                cout<<"Count Function Called - Number of items in the Stack are "<<s1.count()<<endl;
                break;
            case 7:
                cout<<"Change Function Called - "<<endl;
                cout<<"Enter position of item you want to change: ";
                cin>>position;
                cout<<endl;
                cout<<"Enter value of item you want to change: ";
                cin>>value;
                s1.change(position, value);
                break;
            case 8:
                cout<<"Display Function Called - "<<endl;
                s1.display();
                break;
            case 9:
                system("cls");
                break;
            default:
                cout<<"Enter Proper Option Number "<<endl;
        }

    }while(option!=0);


    return 0;
}
//Stack data structure is a linear data structure which operates in a (Last In First Out) or (First In Last Out) pattern.

    //Items are added on top of the stack . This is known as the push operation
    // Items are removed from the top of the stack. This is known as the pop operation.


/*Standard Stack Operations -

1) push() - Place an item on top of the stack. If there is no place for new item, stack is an overflow state.
2) pop() - Return the item at the top of the stack and then remove it. If pop is called when stack is empty, it is in an underflow state.
3) isEmpty() - Tells if the stack is empty or not
4) isfull() - Tells if the stack is full or not
5) peek() - Access the item at the i position
6) count() - Get the number of items in the stack
7) change() - Change the item at the i position
8) display() - Display all items in the stack

*/

/* Applications of Stack Data Structure:
    - Balancing of Symbols
    - Infix to Postfix/Prefix conversion
    - Redo-undo features at many places like editors, photoshop
    - Forward and backward feature in web browsers
    - Used in many algorithms like Tower of Hanoi, tree traversals, stock span problem, histogram problem
    - Other applications can be Backtracking, Knight tour problem, rat in a maze, N queen problem and sudoku solver
    - In Graph Algorithms like Topological Sorting and Strongly Connected Components
*/
