#name = input()
#print(type(input()))

mark1 = input()
mark2 = input()
print(type(mark1))
print(int(mark1) + int(mark2))
------
int[] marks = new int[5]; 
		int total = 0; 
		int max_score = 100; 
		Scanner scanner = new Scanner(System.in); 
		System.out.println("Enter Marks: ");
		for(int i=0; i<marks.length;i++)
		{
		marks[i] = scanner.nextInt(); 
			if(marks[i]<max_score)
			{
				max_score = marks[i];
			}
		total = total + marks[i];
		}
		System.out.println(max_score);
		System.out.println(total/marks.length);
		
		scanner.close();
