#include <iostream>
#include <string.h>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

struct course_datatype
{
	public:
		string course_code;
		float course_credits;
		string course_name;
};

struct student_datatype
{
	public:
		string firstname;
		string lastname;
		string dept;
		string rollno;
		vector<course_datatype> courses_taken;
};

class studentdb
{
	public:
		char * dbname;
		vector<student_datatype> student;
		vector<course_datatype> courses;
		studentdb(string);
		void add_student();
		void delete_student();
		void save();
};

studentdb::studentdb(string dbname_str)
{
	dbname = new char [dbname_str.length()+1];
	strcpy(dbname,dbname_str.c_str());
}

void studentdb::add_student()
{
	student_datatype newstudent;
	cout << "New Student" << endl;
	cout << "(Enter all data in allcaps)" << endl;
	cout << "First name : ";
	getline(cin, newstudent.firstname);
	cout << "Last name : ";
	getline(cin, newstudent.lastname);
	cout << "Roll no. : ";
	getline(cin, newstudent.rollno);
	int duplicate_name = 0;
	int duplicate_rollno = 0;
	for(int a=0;a<student.size();a++)
	{
		if(newstudent.firstname == student[a].firstname && newstudent.lastname == student[a].lastname)
		{
			duplicate_name = 1;
			break;
		}
		if(newstudent.rollno == student[a].rollno)
		{
			duplicate_rollno = 1;
			break;
		}
	}
	if(duplicate_name == 1) cout << "Student name already exists" << endl;
	else if(duplicate_rollno == 1) cout << "Student roll no. already exists" << endl;
	else
	{
		cout << "Department : ";
		getline(cin, newstudent.dept);
		cout << "Courses taken (Enter course codes without spaces) : " << endl;
		string add_course = "Y";
		while(add_course == "Y")
		{
			course_datatype newcourse;
			cout << "Course code : ";
			getline(cin, newcourse.course_code);
			int coursefound = 0;
			int b;
			for(b=0;b<courses.size();b++)
			{
				if(newcourse.course_code == courses[b].course_code)
				{
					coursefound = 1;
					break;
				}
			}
			int coursetaken = 0;
			for(int c=0;c<newstudent.courses_taken.size();c++)
			{
				if(newcourse.course_code == newstudent.courses_taken[c].course_code)
				{
					coursetaken = 1;
					break;
				}
			}
			if(coursetaken == 1) cout << "Course already added to student" << endl;
			else if(coursefound == 1) newstudent.courses_taken.push_back(courses[b]);
			else
			{
				cout << "Course credits : ";
				string credits_str;
				getline(cin, credits_str);
				stringstream(credits_str) >> newcourse.course_credits;
				cout << "Course name : ";
				getline(cin, newcourse.course_name);
				courses.push_back(newcourse);
				newstudent.courses_taken.push_back(newcourse);
			}
			cout << "Add course? (Y/N) : ";
			getline(cin, add_course);
		}
		student.push_back(newstudent);
		cout << "New student added" << endl;
	}
}

void studentdb::delete_student()
{
	cout << "Delete student by :" << endl;
	cout << "1) Name" << endl;
	cout << "2) Roll no." << endl;
	cout << "Enter serial no. : ";
	int deleteby;
	string deleteby_str;
	getline(cin, deleteby_str);
	stringstream(deleteby_str) >> deleteby;
	if(deleteby==1)
	{
		string del_firstname, del_lastname;
		cout << "First name : ";
		getline(cin, del_firstname);
		cout << "Last name : ";
		getline(cin, del_lastname);
		int delstudent_found = 0;
		int d;
		for(d=0;d<student.size();d++)
		{
			if(del_firstname == student[d].firstname && del_lastname == student[d].lastname)
			{
				delstudent_found = 1;
				break;
			}
		}
		if(delstudent_found == 1)
		{
			student.erase(student.begin()+d);
			cout << "Student deleted" << endl;
		}
		else cout << "Name not found" << endl;
	}
	else if(deleteby==2)
	{
		string del_rollno;
		cout << "Roll no. : ";
		getline(cin, del_rollno);
		int delstudent_found = 0;
		int e;
		for(e=0;e<student.size();e++)
		{
			if(del_rollno == student[e].rollno)
			{
				delstudent_found = 1;
				break;
			}
		}
		if(delstudent_found == 1)
		{
			student.erase(student.begin()+e);
			cout <<"Student deleted" << endl;
		}
		else cout << "Roll no. not found" << endl;
	}
}

// Saves database in a file in the pwd with name same as database name

void studentdb::save()
{
	ofstream myfile;
	myfile.open(dbname);
	if(myfile.is_open())
	{
		myfile << "COURSES :" << endl;
		for(int f=0;f<courses.size();f++) myfile << courses[f].course_code << " " << courses[f].course_credits << " " << courses[f].course_name << endl;
		myfile << endl;
		myfile << "STUDENTS :" << endl << endl;
		for(int g=0;g<student.size();g++)
		{
			myfile << g+1 << ")" << endl;
			myfile << student[g].firstname << " " << student[g].lastname << endl;
			myfile << student[g].dept << " : " << student[g].rollno << endl;
			myfile << "Courses taken :" << endl;
			for(int h=0;h<student[g].courses_taken.size();h++) myfile << student[g].courses_taken[h].course_code << " " << student[g].courses_taken[h].course_credits << " " << student[g].courses_taken[h].course_name << endl;
			myfile << endl;
		}
		myfile.close();
		cout << "Database saved" << endl;
	}
	else cout << "Unable to save database" << endl;
}

int main()
{
	cout << "Database name : ";
	string newdbname;
	getline(cin, newdbname);
	studentdb newdb(newdbname);
	string exit = "N";
	while(exit=="N")
	{
		int choose;
		string choose_str;
		cout << "Choose action :" << endl;
		cout << "1) Add student to database" << endl;
		cout << "2) Delete student from database" << endl;
		cout << "3) Save database" << endl;
		cout << "Enter serial no. : ";
		getline(cin, choose_str);
		stringstream(choose_str) >> choose;
		if(choose==1) newdb.add_student();
		else if(choose==2) newdb.delete_student();
		else if(choose==3) newdb.save();
		cout << "Exit? (Y/N) : ";
		getline(cin, exit);
	}
	return 0;
}
