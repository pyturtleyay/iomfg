#![allow(unused)]
use rand::Rng;
use std::io;

use std::cmp::Ordering;
use std::fs::File;

fn main() {
    let mut list  = vec![1,2,3,4,5,6];
    for i in &list{
        list[i] = list[i]*list[i];
    }
    println!("{:?}", list);

}

// println!("What is youre name?");
// let mut name: String = String::new();
// let greeting: &str = "nice to meet you";
// io::stdin()
//     .read_line(&mut name)
//     .expect("Didn't receive Input");

// println!("Hello {}!{}", name.trim_end(), greeting);

    // let sum: i64 = vec![12, 13, 14, 15, 16, 17, 18, 19, 20].iter().fold(1, |acc, x| acc*x);
    
    
    // // let mut sum:i32 =0;
    // // for i in list {
    // //     sum += i;
    // // }
    // println!("{:0.1}", sum);