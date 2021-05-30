import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


import java.util.AbstractQueue;

    /*
     * Complete the 'minimumDistance' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY area as parameter.
     */
    

        
public class OrderDeliveryRoute {
	
	
    public static int minimumDistance(List<List<Integer>> area) {
    // Write your code here
        int rows = area.size();
        int cols = area.get(0).size();
        int startr =0 , startc = 0;
        Queue<Integer> qr = new LinkedList<>();
        Queue<Integer> qc = new LinkedList<>(); 
        int distance = 0 ;
        boolean foundans = false;
        boolean check[][] = new boolean[rows][cols];
        int nlp =1 ;
        int nnp = 0; 
        
        qr.add(startr);
        qc.add(startc);
        check[startr][startc]=true;
        
        //if (area.get(0).get(0)==9) return 1;
        //if (area.get(0).get(0)==0) return -1;
        //area.get(startr).set(startc , 0);
        
        while(qr.size()>0){
            int currentr = qr.poll();
            int currentc = qc.poll();
            if (area.get(currentr).get(currentc)==9 ){
                foundans =true;
                break;
            }
            int directions[][] = new int[][]{{-1,0} ,{1,0}, {0,1} , {0,-1}};
            for(int i= 0 ; i<4 ; i++){
                int newr = currentr + directions[i][0];
                int newc = currentc + directions[i][1];
            
                if (newr<0 || newr>=rows) continue;
                if (newc<0 || newc>=cols) continue;
                if (check[newr][newc]) continue;
                if (area.get(newr).get(newc)==0) continue;
            
                qr.add(newr);
                qc.add(newc);
                check[newr][newc]=true;
                nnp++;
            
            
        }
        
        nlp--;
        
        
            if (nlp==0){
                nlp = nnp;
                nnp = 0;
                distance++;
            }
            
        }
        
        if (foundans==true) return distance;
        return -1;
        
    }
	
	
	public static void main(String[] args) {
		List<Integer> l1=new ArrayList<Integer>(){{
            add(1);
            add(0);
            add(0);
              }};
              
  		List<Integer> l2=new ArrayList<Integer>(){{
            add(1);
            add(0);
            add(0);
              }};
                  
                  
  		List<Integer> l3=new ArrayList<Integer>(){{
            add(1);
            add(9);
            add(1);
              }};
              
              
  		List<List<Integer>> l4=new ArrayList<List<Integer>>(){{
            add(l1);
            add(l2);
            add(l3);
              }};
		System.out.println(minimumDistance(l4));
	}
}
