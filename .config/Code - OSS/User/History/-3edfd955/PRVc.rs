#![allow(unused)]
use rand::Rng;
use std::io;

use std::cmp::Ordering;
use std::fs::File;

fn main() {
    vec![1, 2, 3, 4, 5, 6]
        .iter()
        .enumerate()
        .for_each(|(i, x)| println!("{i}-->{x}"));
    // for (i, elements) in list.iter().enumerate(){ca
    //     println!("Indice : {} --> {}", i, elem);
    // }
}
//     let list: Vec<i32> = vec![1, 2, 3, 4, 5, 6].iter().map(|x| x * x).collect();

//     println!("{:?}", list)
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