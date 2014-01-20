

use <geisel/screws.scad>

module ring( ) {
	import("verlichting_3d_printer.stl");
}

module halterung() {
	// h = 16 mm
	// y = 50 mm
	// x = 20 + 10 = 30 mm 
	
	difference() {
		union() {			
			scale(v = [10, 10, 10])	
				import("verlichting_3d_printer_bevestiging.stl");
			translate([-30,20,0])
				cube([10,10,16]);
		}
		
		translate([-20,25,16])
			rotate([180,0,0])
				#schraube();
	}
}


module all() {
	rotate([0,0,2])ring();
	
	*#translate([-60,-25,20])
		rotate([-180,0,180])
			 halterung();
}






module cutOffRing(){
	difference(){
		cylinder(r=41.5, h=1.5, $fn=60);
		translate([0,0,-1])
			cylinder(r=39.5, h=5, $fn=60);
			
		translate([40,0,0.8])
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
ledRadius = 2.55;
module newRing() {
	difference() {
		cylinder(r=43, h=3, $fn=60);
		translate([0,0,-1])
			cylinder(r=30, h=5, $fn=60);
		
		translate([0,0,-5])
			leds(27.7, ledRingRadius);
			
		translate([ledRingRadius,0,-3])
			schraube();
		
		translate([0,0,1.6])
			cutOffRing();
	}
}

newRing();

//%all();
//*%translate([-30,0,0])
//	cube([30,50,16]);
//*#halterung();