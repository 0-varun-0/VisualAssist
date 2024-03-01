package com.example.visualassist
import android.Manifest
import android.app.Activity
import android.content.Context
import android.content.pm.PackageManager
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

class requestPermission {

    object CameraPermissions {
        const val REQUEST_CODE = 100

        fun checkPermission(context: Context): Boolean {
            return ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED
        }

        fun requestPermission(activity: Activity) {
            ActivityCompat.requestPermissions(activity, arrayOf(Manifest.permission.CAMERA), REQUEST_CODE)
        }
    }
}