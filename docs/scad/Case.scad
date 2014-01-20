
use <geisel/screws.scad>

// Case 
//
// breite = 60 mm
// länge = 50mm
// höhe = 15 mm
module case() {
	cube([60,50,15]);
}


module raspberryMount() {
	cube([80,4,4]);
	
	cube([80,4,4]);
}

module switch() {
	translate([0,0,4.27])
		union() {
			color("darkgray")cube(8.54, center=true);
			
			color("black") {
				translate([0,0,5.52])
					cube([4,3.9,2.5], center=true);
			
				translate([0,0,8.37])
					cube([3,2,3.1], center=true);
			}
		}
}

module Button() {
	difference(){
		cylinder(r=8, h=3.55, $fn=120,center=true);
					
		translate([0,0,-0.3])
					cube([3.5,2.5,3.1], center=true);
	}
}

!Button();
translate([0,0,-15])
	switch();
	