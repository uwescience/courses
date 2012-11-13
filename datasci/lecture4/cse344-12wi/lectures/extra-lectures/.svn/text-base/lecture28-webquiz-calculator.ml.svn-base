(* f computes the probability that a pair of documents do NOT have a common signature *)

let f r s = (1.0 -. s**r)**(24.0/.r);;

(* the false positive fraction is: *)

let fp r = 1.0 -. (f r 0.2);;

(* the false negative fraction is: *)

let fn r = (f r 0.5);;

(* let M = c*N;  c is given by the problem and is 1, 10, 100, etc *)

let c = 1000.0;;

(* cost = fn*N + np*M = (fn + c*fp) * N *)

let cost r = (fn r) +. (c *. (fp r));;

let rr = [1.0; 2.0; 3.0; 4.0; 6.0; 8.0; 12.0; 24.0];;

let g r = (fn r, fp r, cost r);;

let _ = List.map g rr;;
