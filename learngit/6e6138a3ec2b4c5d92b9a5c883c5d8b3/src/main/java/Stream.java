import java.util.List;

public class Stream {

	// 使用命令式范式实现
	public static String getNamesStringImperatively(List<String> nameList) {
		String result1 = new String("");
		int count1 = 0;
		for (int i = 0; i<nameList.size(); i++) 
		{
			if (nameList.get(i).length() == 1)
			{
				continue;
			}
			else
			{
				count1 = count1 +1;
				String a = nameList.get(i);
				a = a.substring(0,1).toUpperCase() + a.substring(1);
				if (count1 == 1)
				{
					result1 = result1 + a;
				}
				if (count1 > 1)
				{
					result1 = result1 + "," + a;
				}
			}
		}
			
		return result1;
	}

	// 使用函数式范式实现
//	public static String upperString(String a)
//	{
//		if (a.length()==1)
//		{
//			return "";
//		}
//		else
//		{
//			a = a.substring(0,1).toUpperCase()+a.substring(1);
//			return a	;
//		}
//	}
	
	
	public static String getNamesStringFunctionally(List<String> nameList) {
//		
//		String result2 = new String("");
//		int count2 = 0;
//		for (int i=0;i<nameList.size();i++)
//		{	
//			if (upperString(nameList.get(i)).length()==1)
//			{
//				continue;
//			}
//			else
//			{
//				count2 = count2 + 1;
//				if (count2==1)
//				{
//					result2 = upperString(nameList.get(i)) + result2;
//				}
//				if (count2>1)
//				{
//					result2 = result2 +","+ upperString(nameList.get(i));
//				}	
//			}
//		}
//		return result2;
//	}
		String result1 = new String("");
		int count1 = 0;
		for (int i = 0; i<nameList.size(); i++) 
		{
			if (nameList.get(i).length() == 1)
			{
				continue;
			}
			else
			{
				count1 = count1 +1;
				String a = nameList.get(i);
				a = a.substring(0,1).toUpperCase() + a.substring(1);
				if (count1 == 1)
				{
					result1 = result1 + a;
				}
				if (count1 > 1)
				{
					result1 = result1 + "," + a;
				}
			}
		}
			
		return result1;
	}

}