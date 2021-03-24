# HypoNPAtlas server
## Introduction
The [hypoNPAtlas](http://metabologenomic.cbd.cs.cmu.edu/AtlasofHypotheticalMolecules/) webserver currently includes hypothetical RiPPs from 22,671 complete microbial genomes from RefSeq. Users can select specific strains / taxonomic clades and download the corresponding BGC, ORF, core and molecular structure data. Additionally, the hypoNPAtlas webserver supports the processing of input genomic data from users. The fragmentation of all the molecular structures are prepossessed and available from the server, and the users can retrieve a token string corresponding to their genome of interest, which can be searched against mass spectral datasets using Dereplicator+ from the [GNPS](https://gnps.ucsd.edu/ProteoSAFe/index.jsp) infrastructure. This design strategy provides two benefits: (i) by using preprocessed fragmentation graphs instead of molecular structures in SMILES format, Dereplicator+ search will be orders of magnitude faster, and (ii) using a token string (rather than downloading and uploading preprocessed fragmentation graphs) facilitates the interaction between hypoNPAtlas (responsible for genome mining) and the [GNPS](https://gnps.ucsd.edu/ProteoSAFe/index.jsp) infrastructure (responsible for mass spectral search).


[HypoNPAtlas](http://metabologenomic.cbd.cs.cmu.edu/AtlasofHypotheticalMolecules/) was built using Shiny, an R package developed to simplify the complexities of typical back and front-end web development. Shiny requires two scripts, ui.R and server.R that control the appearance of the app and contain functionality needed to build the app, respectively. HTML, CSS, and Javascript can be added to both scripts to extend R functionality, and snippets of all three languages were used in areas where R lacked methods for a requirement, including loaders, view buttons, and row conditions within data tables. On the back-end, genomic data for BGCs, ORFs, cores, and RiPPs are separated by files. The architecture of hypoNPAtlas requires a one-to-one mapping of genomes to data directories. A directory containing 4 files, one for each type of sequence in the seq2ripp pipeline, maps to a single genome. HypoNPAtlas is hosted on an Ubuntu server at Carnegie Mellon University.

## How to use your own data on hypoNPAtlas server
To run the seq2ripp pipeline on your own data, please visit [hypoNPAtlas](http://metabologenomic.cbd.cs.cmu.edu/AtlasofHypotheticalMolecules). From there, navigate to the upload tab using the menu. Seq2ripp requires an input genome and email to run. Upon hitting the run button, the genome will be read to look for any unknown characters or unreadable data. Here is the explanation step by step:

* The homepage of the server. Navigate to the upload page by clicking the uplaod button in the sidebar.
<img src="/imgs/sfig7a.png" alt="webserver"  width="500">
* The upload page, where you can upload your genome and fill out your contact email address.
<img src="/imgs/sfig7b.png" alt="upload genome"  width="500">
* This might take a few seconds to upload and cleaning the file. After it's done, you will see the message at the bottom.
<img src="/imgs/sfig7c.png" alt="genome uploaded"  width="500">
* After around 30 minutes, you will receive this email in the mailbox of the email address you provided. The 50 digits token is used for the GNPS, which will be explain in the next step. Also, you will receive the link to download the BGC, ORF, core, and the molecules in SMILES format.
<img src="/imgs/sfig7d.png" alt="email"  width="500">

## How to use GNAS
After validation, users will see a message telling them to check their email for a message from someone at metabologenomic.cbd.cs.cmu.edu. This email will contain a run ID that will be used as input to Dereplicator+. The processed data contains the hypothetical RiPPs. Dereplicator+ matches molecules to a mass spectra of interest. Users interested in taking their seq2ripp outputted molecules and matching them against mass spectra will upload or choose available mass spectra at [GNPS](https://gnps.ucsd.edu/ProteoSAFe/index.jsp) and type their run ID (from their email) as the custom DB URL parameter. Dereplicator+ will then search for unique and significant metabolite matches and output them to the user.

* Navigate down to the Advanced Analysis Tools section, and click "Browse Tools" In Silico Tools.
<img src="/imgs/sfig7g.png" alt="Advance tool"  width="500">
* Click the link "here" in the Dereplicator+ at the left bottom.
<img src="/imgs/sfig7h.png" alt="dereplicator+"  width="500">
* In advanced options, please fill the 50 digit token to the custom DB URL.
<img src="/imgs/sfig7e.png" alt="db link"  width="500">
* After a few hours, you will receive an email from GNPS, and a link to the result.
<img src="/imgs/sfig7f.png" alt="GNPS results"  width="500">
