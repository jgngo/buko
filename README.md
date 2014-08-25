buko
====

BUKO Project

Buko is a low-cost, self-sufficient, wirelessly accessed, electronic library with curated content from the best educational-initiatives online – a hub of learning without the Internet.

This project is based on the RACHEL server distribution which is part of the [RACHEL Project](http://pi.worldpossible.org/), an initiative to make available rich and curated educational content to places where no Internet connectivity is available or the available bandwidth is unusable for most practical purposes.

Each piece of educational content is owned by the owners listed next to the content title in the RACHEL main page.

Boundless Knowledge Offline

This project is an offline and compact compilation of educational content containing more than 2,000 selected Khan Academy video lectures on Math and Science, ebooks from OLPC, CK-12 Project Gutenburg, and organized by Philippine educators in a very user-friendly format. The content can be viewed and played on modern HTML5 browsers desktop computers and mobile devices like iPads, iPhones and Android devices.

* Installation

Download the update file (buko_yyyymmdd) that replaces the default Rachel contents to BUKO. 
For now, this needs to be done manually but a script could potentially work. Connect to the by wifi to RPI:

1. copy the zip file using sftp://192.168.10.1
2. ssh to 192.168.10.1 (user:pi password:rachel)
3. unzip buko_yyyymmdd.zip
4. cd /var
5. sudo chown pi:pi www
6. cd www
7. sudo cp -R ~/buko/* .
8. cp img/favicon.ico .

After this, going to 192.168.10.1 will show the new page.
