/**
 * The following is an implementation of K Nearest Neighbour algorithm in C++
 */
#include <iostream> // supports cin(), cout()
#include <string> // supports string data type
#include <cmath> // supports sqrt(), pow()
#include <algorithm> // supports sort()

using namespace std;

#define SIZE 4 // size of array

struct Data {
  string nme; // name
  double dur, str; // acid durability, strength
  string cls; // class
  double dst; // distance
};

bool wayToSort(Data x, Data y) {  return x.dst < y.dst; }

int main() {
  int k = 1;
  Data training[SIZE];
  Data actual;

  /* training data */
  training[0].nme = "Type-1";
  training[0].dur = 7;
  training[0].str = 7;
  training[0].cls = "Bad";

  training[1].nme = "Type-2";
  training[1].dur = 7;
  training[1].str = 4;
  training[1].cls = "Bad";

  training[2].nme = "Type-3";
  training[2].dur = 3;
  training[2].str = 4;
  training[2].cls = "Good";

  training[3].nme = "Type-4";
  training[3].dur = 1;
  training[3].str = 4;
  training[3].cls = "Good";

  /* new data */
  cout << "Enter the following information." << endl << endl;

  cout << "Enter the Type: ";
  cin >> actual.nme;

  cout << "Enter the Acid Durability: ";
  cin >> actual.dur;

  cout << "Enter the Strength: ";
  cin >> actual.str;

  /* calculate euclidean distance */
  for (int i = 0; i < SIZE; i++) {
    training[i].dst = sqrt( pow((training[i].dur - actual.dur), 2) + pow((training[i].str - actual.str), 2) );
  }

  /* sort array in ascending order */
  sort(training, training+SIZE, wayToSort);

  /* select K nearest neighbours */
  cout << endl << "Enter K: ";
  cin >> k;

  int good = 0, bad = 0;

  /* determine frequency of the class values */
  for (int j = 0; j < k; j++) {
    if (training[j].cls == "Good") good++;
    else if (training[j].cls == "Bad") bad++;
  }

  /* print class value with the highest frequency */
  cout << endl << "The class is: " << (good >= bad ? "Good" : "Bad") << endl;

  return 0;
}
