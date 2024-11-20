#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

int main() {
    // Create a VideoCapture object to represent the webcam
    cv::VideoCapture cap;
    // Open the webcam using the default index (usually the built-in webcam)
    cap.open(0);

    // Check if the webcam is open
    if(!cap.isOpened()) {
        std::cout << "Error opening webcam!" << std::endl;
        return -1;
     }

    // Create a window to display the video
   cv::namedWindow("Webcam", cv::WINDOW_AUTOSIZE);

   // Create a Mat object to store each frame of the video
   cv::Mat frame;

   // Continuously capture and display video from the webcam
   while(1) {
       // Capture a new frame from the webcam
       cap >> frame;
       // Display the frame in the window
       cv::imshow("Webcam", frame);
       // Wait for the user to press a key before capturing the next frame
       if (cv::waitKey(1) >= 0) break;
    }

    // Release the webcam and destroy the window when you are done using it
    cap.release();
    cv::destroyWindow("Webcam");
    return 0;
}
