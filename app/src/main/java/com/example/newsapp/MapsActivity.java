package com.example.newsapp;

import androidx.fragment.app.FragmentActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.Circle;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import static java.security.AccessController.getContext;

public class MapsActivity extends FragmentActivity implements
        OnMapReadyCallback,
        GoogleMap.OnCameraMoveStartedListener,
        GoogleMap.OnCameraMoveListener,
        GoogleMap.OnCameraMoveCanceledListener,
        GoogleMap.OnCameraIdleListener {

    private GoogleMap mMap;
    //private Circle circle;
    private Marker marker;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // Add a marker in Sydney and move the camera
        LatLng sydney = new LatLng(-34, 151);

        final LatLng london = new LatLng(51.5, -0.12);

        marker = mMap.addMarker(new MarkerOptions().position(london).title("Marker in London"));

        CircleOptions circleOptions = new CircleOptions()
                .center(sydney)
                .radius(100000)
                .fillColor(Color.RED);

        Circle circle = mMap.addCircle(circleOptions);

        mMap.moveCamera(CameraUpdateFactory.newLatLng(london));
        //mMap.setOnCameraMoveListener(new GoogleMap.OnCameraMoveListener() {
          //  @Override
            //public void onCameraMove() {
              //  Toast.makeText(getApplicationContext(),
                //        "Camera Moved",
                  //      Toast.LENGTH_SHORT).show();
            //}
        //});

        mMap.setOnCameraIdleListener(new GoogleMap.OnCameraIdleListener() {
            @Override
            public void onCameraIdle() {
                inOrOut(london); //checks if marker is visible on screen
                //displayMoveMessage();//camera moved, display moved msg
            }

        });
    }

    public void displayMoveMessage(){
        Toast.makeText(getApplicationContext(),
                "Camera Moved",
                Toast.LENGTH_SHORT).show();
    }

    public void inOrOut(LatLng position){

        //check if a specific latlong position exists within current map view or not
        if (!mMap.getProjection().getVisibleRegion().latLngBounds.contains(position))
        {
            //marker.remove();//this removes the marker as soon as it disappears from screen
            Toast.makeText(getApplicationContext(),
                    "London not visible",
                    Toast.LENGTH_SHORT).show();

            //make a marker at current position at middle of map
            LatLng center = mMap.getCameraPosition().target;
            if (marker!=null){
                marker.remove();
                marker = mMap.addMarker(new MarkerOptions().position(center).title("New Position"));
            }

        }
    }

    @Override
    public void onCameraIdle() {

    }

    @Override
    public void onCameraMoveCanceled() {

    }

    @Override
    public void onCameraMove() {

    }

    @Override
    public void onCameraMoveStarted(int i) {

    }
}
