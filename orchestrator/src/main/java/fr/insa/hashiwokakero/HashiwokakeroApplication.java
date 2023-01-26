package fr.insa.hashiwokakero;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.openfeign.EnableFeignClients;


@SpringBootApplication
@EnableFeignClients
public class HashiwokakeroApplication {

	public static void main(String[] args) {
		SpringApplication.run(HashiwokakeroApplication.class, args);
	}


}
