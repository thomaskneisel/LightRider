

use <geisel/screws.scad>

module cutOffRing(raduis){
	difference(){		
		cylinder(r=raduis, h=1.5, $fn=60);
		translate([0,0,-1])
			cylinder(r=raduis-2, h=5, $fn=60);
			
		translate([raduis-1.5,0,0.8])
			cube([5,20,2],center=true);
	}
}

module leds(degrees, radius) {
	for (alpha = [degrees:degrees:360]) {
		translate([radius*cos(alpha), radius*sin(alpha), 0])
			cylinder(r=ledRadius, h=10, $fn=60);
	}
}

ledRingRadius = 35;
ledRadius = 2.68;
module ring() {
	difference() {
		cylinder(r=43, h=3, $fn=90);
		translate([0,0,-1])
			cylinder(r=30, h=5, $fn=90);
		
		translate([0,0,-5])
			leds(27.7, ledRingRadius);
			
		translate([ledRingRadius,0,-3])
			schraube();
		
		translate([0,0,1.6])
			cutOffRing(41.5);
			
		*translate([0,0,2])
			difference() {
				cutOffRing(ledRingRadius+1);
				translate([-ledRingRadius+0.5,0,0.8])
					cube([5,15,2],center=true);
			}
	}
}

module mounting_raw() {
	union() {
		translate([0,0,0.1])
			cube([10,19,16], center=true);
		translate([15,0,7])
			cube([20,50,2.2], center=true);
		
		translate([-2,0,0])
			difference() {
				translate([10,0,4])
					rotate([0,0,0])
						cube([6,19,6], center=true);
						
				translate([13.2,0,1])
					rotate([0,45,0])
						cube([9,20,9], center=true);
			}
		
		translate([5.6,9.1,7])
			rotate([0,0,45])
				cube([15,15,2.2], center=true);
			
		translate([5.6,-9.1,7])	
			rotate([0,0,-45])
				cube([15,15,2.2], center=true);
	}
}

module mounting() {
	difference() {
		translate([35,0,11])
			mounting_raw();
			
		translate([35,0,14.9]) {
			rotate([180,0,90]) {
				schraube();
				translate([0,0,-2.3])
					schraube();
				translate([0,0,-4.3])
					schraube();
			}
		}
		
		translate([35,0,10]) 
			cylinder(r1=1.7, r2=3, h=2.5,$fn=60);
		
		translate([50,15,13]) {
			cylinder(r=4.5,h=5, $fn=90);
			translate([0,0,2]) 
				cylinder(r=3.35,h=5, $fn=90);
		}
		
		translate([50,-15,13]) {
			cylinder(r=4.5,h=5, $fn=90);
			translate([0,0,2]) 
				cylinder(r=3.35,h=5, $fn=90);
		}
		
	}
	
}

// Layouts	

LAYOUT="PintTestRing";
LAYOUT="ring";
LAYOUT="mounting";
//LAYOUT="all";
//LAYOUT="dev";

if(LAYOUT=="PintTestRing") {
	intersection(){
		ring();
		translate([25,2,0])
			cube([20,20,4]);
	}
}

if(LAYOUT=="ring") {
	!ring();
}

if(LAYOUT=="mounting") {
	//!rotate([180,0,0])
		mounting();
}

if(LAYOUT=="all") {
	ring();
	mounting();
}

if(LAYOUT=="dev") {
	ring();
	mounting();
}