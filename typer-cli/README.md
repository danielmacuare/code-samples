# Typer-CLI Sample

In this repo we will create a Python CLI App to test Typer's Commands, Sub-commands, Options and Arguments.

More information about this code can be found on the following blog post: LINK

The way this app has been created is by breaking down each cli command in  a single file. For example, we will use 4 different commands for our CLI App:

- discover: This will discover all the network devices and saved them to a local Database.
- add: This will add all the discovered devices from the local database into Netbox. You can also add a single device out of the DB into Netbox
- show: This command will show devices and subnets available in Netbox and the local database.
- delete: will delete all-devices or a single device from netbox.

We will call our main file and we will pass any of the 4 commands above.

**note:** This repo doesn't include any data validations, testing, etc. The idea of this repo is only test how to use Typer to break down your CLI app and make it modular.

## How To use

- Clone the repo: `git@github.com:danielmacuare/code-samples.git`
- Get into the src folder: `cd typer-cli/src/`
- Run any of the following commands:

### add command

```bash
python main.py add --help
python main.py add --discovered-devices
python main.py add --single-device chi-leaf-04
python main.py add -d
python main.py add -s chi-leaf-04
```

### discover command

```bash
python main.py discover --help
python main.py discover subnet 10.1.1.0/24
python main.py discover device chi-leaf-04
```

### delete command

```bash
python main.py delete --help
python main.py delete --all-devices --dry-run
python main.py delete --single-device fra-fw-02
python main.py delete -ad
python main.py delete -s fra-fw-02
```

### show command

```bash
python main.py show --help
python main.py show netbox --help
python main.py show netbox devices
python main.py show netbox subnets
python main.py show discovered --help
python main.py show discovered devices
python main.py show discovered subnets
```

## TO-DO

- Create a Link to the blog post
