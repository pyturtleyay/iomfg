#![allow(unused)]
use rand::Rng;
use std::io;

use std::cmp::Ordering;
use std::fs::File;

// def reverse(list):
//     for i in range len(list)
//         list[i] = list[len(list)-i]
//     return list;

// fn reverse(mut list: Vec<i32>) -> Vec<i32>{
//     let mut list2 = Vec::new();
//     for i in 0..list.len(){
        
//         list2.push(list[list.len()-i-1]);
        
//     }

//     list2
// }
fn main() {
    
    //vec![1, 2, 3, 4, 5, 6]
    //     .iter()
    //     .enumerate()
    //     .for_each(|(i, x)| println!("{i}-->{x}"));
    // for (i, elements) in list.iter().enumerate(){ca
    //     println!("Indice : {} --> {}", i, elem);
    // }
}//
    let list: Vec<i32> = vec![1, 2, 3, 4, 5, 6];
    let mut list2 = Vec::new();
    for i in 0..list.len(){
        if i%2==0{
            list2.push(list[i]-1);
        }
        else{
            list2.push(list[i]+1);
        }

    }
    // def divisoin(input):
    // 
//     println!("{:?}", list)
// println!("What is youre name?");
// let mut name: String = String::new();
// let greeting: &str = "nice to meet you";
// io::stdin()
//     .read_line(&mut name)
//     .expect("Didn't receive Input");

// println!("Hello {}!{fn main() {}", name.trim_end(), greeting);

// let sum: i64 = vec![12, 13, 14, 15, 16, 17, 18, 19, 20].iter().fold(1, |acc, x| acc*x);

// // let mut sum:i32 =0;
// // for i in list {
// //     sum += i;
// // }
// println!("{:0.1}", sum);
