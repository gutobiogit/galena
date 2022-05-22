<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Galena challenger</h3>

  <p align="center">
    Galena Challenger is a CRUD system that uses excel file as db
    <br />
    <a href="https://github.com/gutobiogit/galena/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/gutobiogit/galena">View Demo</a>
    ·
    <a href="https://github.com/gutobiogit/galena/issues">Report Bug</a>
    ·
    <a href="https://github.com/gutobiogit/galena/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [python](https://www.python.org/)
* [http.server](https://docs.python.org/3/library/http.server.html/)
* [docker](https://www.docker.com/)
* [google tag](https://tagmanager.google.com/)
* [Bootstrap](https://getbootstrap.com/)
* [sweet alert](https://sweetalert.js.org/guides/)

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* git
  ```sh
  sudo apt install git
  ```

* docker
  ```sh
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
  ```


<!-- GETTING STARTED -->
## Getting Started

* To test the project you first have to clone it
    ```sh
     git clone git@github.com:gutobiogit/galena.git
    ```

* Build the docker container image
    ```sh
    docker image build -t galena_challenger .
    ```

* Run the container
```sh
docker run -p 5500:5500 -p 5000:5000 --mount type=bind,source="$(pwd)"/src/database,target=/app/src/database/ galena_challenger
```



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Open a browser in http://127.0.0.1:5500/
<br>
The used .xlsx file is located at src/database, it persists even when the container is terminated.
<br>
If you want to use another .xlsx file just change the file.
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/gutobiogit/galena/fork
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
