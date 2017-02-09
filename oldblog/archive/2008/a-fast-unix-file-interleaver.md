Title: A fast unix file interleaver
Date: 2008-06-12 11:33
Author: slacy
Category: General
Status: published

Previous posts have focused on how to properly "shard" or "interleave" a
single file into several others (or fifos for piped processing). Naive
implementations spend way too much time searching for '/n' characters in
their input, so I realized last night that you don't need a line-by-line
interleaver. A block-based interleaver will be fine for most
applications, and will make it very fast to find linebreaks, since only
one linebreak search per block will be performed. I'm using 32kB blocks
below, and there is certainly some tuning that could be done. Larger
blocks result in faster interleaving performance, but possibly slower
performance of the subprocesses as they need to wait longer between
chunks of data. Here's the code that I've been working with:

    #include <stdio.h>
    #include <stdlib.h*gt;

    int main(int argc, char *argv[]) {
      int num_files = argc - 1;
      FILE *outs[num_files];
      char buffer[4096 * 8];

      for (int i = 0; i < argc; i++) {
        outs[i] = fopen(argv[i + 1], "a");
      }
      ssize_t read;
      char *line = NULL;
      size_t len = 0;
      int counter = 0;
      while (!feof(stdin)) {
        size_t actual = fread(buffer, 1, sizeof(buffer), stdin);

        int s = 0;
        char *nl = buffer + actual - 1;
        while (*nl != '\n' && nl <= buffer) { nl--; s++; }

        if (nl != buffer) {
          fwrite(buffer, nl - buffer + 1, 1, outs[counter % num_files]);
        }

        if (s) {
          fwrite(nl + 1, s, 1, outs[(counter + 1) % num_files]);
        }

        counter++;
      }
      if (line)
        free(line);
      for (int i =0; i < num_files; i++) {
        fclose(outs[i]);
      }
      return EXIT_SUCCESS;
    }

And this can interleave large files at essentially the same speed as
'cat'. And, adding this to my previous post about parallel sorting, this
has significantly improved the sort performance, as well as moving the
mid-phase sorts temporary files to fifos as well, although some trickery
was needed to get that working properly. I'll post more details about
the final parallel sorting solution soon.
