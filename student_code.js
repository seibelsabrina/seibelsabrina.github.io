// Sabrina Seibel
// seibelsabrina@gatech.edu
// I talked to Octavien Han

kiwi_caught = 0;

function process_frame() {
		num = Math.random();
	if (num*100 < kiwi_rate) {
		create_kiwi();
	}
	if (is_down("b")) {
		brake_truck();
	}
	else if (is_down("left")) {
		translate_truck_left();
	}
	else if (is_down("right")) {
		translate_truck_right();
	}
	else if (is_down("")){
		coast_truck();
	}
	compute_truck_position();
	}


function translate_truck_right() {
	if (get_truck_velocity()<50) {
	set_truck_velocity(get_truck_velocity()+ .5);
}
}

function translate_truck_left() {
	if (get_truck_velocity() > -50) {
	set_truck_velocity(get_truck_velocity() -.5);
}
} 

function coast_truck() {
	if (get_truck_velocity() != 0) {
		set_truck_velocity(get_truck_velocity()*.9);
	}
}

function brake_truck() {
	while (get_truck_velocity() != 0) {
		set_truck_velocity(get_truck_velocity()*.5);
	}
}

function compute_truck_position() {
	var1 = get_truck_left() +get_truck_velocity();
	if (var1  < 0) 
	{
		set_truck_velocity(get_truck_velocity()*-.5);
	}
	else if (var1 >= window.innerWidth - 250) 
	{
		set_truck_velocity(get_truck_velocity()*-.5);
	}
	var1 = get_truck_left() +get_truck_velocity();
	set_truck_left(var1);
}

function find_collisions(kiwi) {
 kiwix = get_kiwi_x(kiwi);
 kiwiy = get_kiwi_y(kiwi);
 truckx = get_truck_left();
 if (truckx > kiwix -125 && truckx <kiwix + 125) {
 	if (kiwiy >window.innerHeight - 20){
 		delete_kiwi(kiwi);
 		kiwi_caught++;
 		document.getElementById("kiwi-count").innerHTML = kiwi_caught;
 	}
 }
 // The kiwi needs to land in the truck bed for it to count as a point. 
// If the x coordinate of the truck is greater than the kiwi's x coordinate minus 
//125 and less than the kiwi's x coordinate plus 125 it means the kiwi is left of
// the front end of the truck and right of where the truckbed ends- meaning it 
// is within the truckbed's x coordinate range.
// Since y is constant, if the kiwi is in the x coordinate range of the truckbed
// and at a 20px height (eyeballed to be about the height where the truckbed begins)
// then it increments kiwi_caught and deletes the kiwi from view.
}

function game_over() {
	alert("Time is Up!", "Congrats, you caught " + kiwi_caught + " kiwis!", "Play again?");
kiwi_caught = 0;
document.getElementById("kiwi-count").innerHTML = kiwi_caught;
}

check_latest = 2;