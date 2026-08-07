---
title: Using a floating license
source: https://docs.kanzi.com/4.1.0/en/installing-kanzi/license-management/floating-license.html
---

# Using a floating license


Your installation of Kanzi Studio can lease a floating license either from:

- The floating license server that Rightware maintains. When you use this option, Rightware carries the maintenance responsibility of your license. You need an internet connection and a properly set up firewall to lease a license from the Rightware floating license server. See Using the Rightware floating license server.
- A floating license server that you set up on any physical computer on your network. See Setting up a floating license server.


If you have a license server installed, but instead of a floating license want to use a product key or a license file, see Using a product key to activate Kanzi Studio and Using a license file to activate Kanzi Studio.

For technical support use the Kanzi Support Portal at [http://support.rightware.com](http://support.rightware.com/). See Technical support.
## Using the Rightware floating license server


If you decide to use the Rightware floating license server, you receive a lic license file from Rightware.

To use the Rightware floating license server:

1.

In a plain-text editor open the lic license file you received from Rightware and configure your firewall to enable Kanzi Studio to use the two TCP ports mentioned in that file.
2.

Open Kanzi Studio and in the License Manager click Next.

If you do not have a valid Kanzi Studio license, Kanzi Studio opens the License Manager. If you already have a working license, but want to switch to a different license type, see Changing the type of Kanzi Studio license.
3.

Select License file and click Next.
4.

Click Browse, select the lic floating license file that you received from Rightware, and click Next.

Kanzi Studio connects to the Rightware floating license server set in the lic file and leases a license.

  - If the license activation is successful, click OK and start using Kanzi Studio.
  - If the license activation was not successful, the License Manager displays a message saying what went wrong.


For technical support use the Kanzi Support Portal at [http://support.rightware.com](http://support.rightware.com/). See Technical support.
## Leasing a floating license


If you are using floating licenses, before you can use Kanzi Studio, Kanzi Studio needs to lease a floating license from a license server. When you are no longer using Kanzi Studio you can release the license so that someone else on your network can use that license. See Releasing a floating license.

To lease a floating license from a license server, open Kanzi Studio:

- If you use the Rightware floating license server, your computer must be able to access the two TCP ports mentioned in the lic license file which you received from Rightware.
- If you use your own floating license server, the computer on which you use Kanzi Studio must be on the same network as your floating license server.


Kanzi Studio automatically finds the license server and, if there are available licenses, leases a license.

With a single floating license you can open at most three instances of Kanzi Studio. If more floating licenses are available on your license server, Kanzi Studio automatically leases an additional license for additional instances of Kanzi Studio.

If you have a license server installed, but instead of a floating license want to use a product key or a license file, see Using a product key to activate Kanzi Studio and Using a license file to activate Kanzi Studio.
## Releasing a floating license


When you are done using Kanzi Studio, you can release the license so that someone else on your network can use it. You can release a floating license on the computer that leased the license, or on the license server.

- To release a floating license, close Kanzi Studio.

When you close Kanzi Studio, it automatically releases the leased license to the license server.
- To release a floating license on your own floating license server:

  1.

On the license server open a web browser and go to http://localhost:5054.

If you are running the license server on a different address, use that address.
  2.

In the left pane click **Status**, and then click the button under **License Usage**.
  3.

Click **GET License Usage**, then click **Remove** next to the license you want to release.


## Setting up a floating license server


You can set up a floating license server on a physical computer running one of these operating systems:

- Windows (32-bit or 64-bit)
- Linux (64-bit)


Firewalls and anti-virus software installed on the license server and computers that use Kanzi Studio floating licenses can affect the communication between Kanzi Studio and the license server. Make sure that you set up the license server on a specific network port and that all computers that need to access the license server can access that port through the firewall and anti-virus software.

To set up a license server:

1.

Install the license server you received from Rightware on any computer on your network.

Because the license of the license server is locked to the hardware ID of the hard disk drive where you install the license server, install the license server on the hard disk drive which you do not intend to replace any time soon.
2.

In the directory where you installed the license server run this command to generate the unique ID for each hard disk drive on the computer where you installed the license server.

```
rlmutil.exe rlmhostid

```

3.

Submit a support request at the Kanzi Support Portal at [support.rightware.com](http://support.rightware.com/) with the hardware ID of the hard disk drive where you installed the license server you generated in the previous step. See Technical support.
4.

After you receive the lic license file from the Rightware support team, place the license file to the same directory where you installed the server.
5.

Run `rlm.exe` to start the license server.

When the server is running, computers on the same network can lease Kanzi Studio licenses from the server. See Leasing a floating license.

The license server comes with an embedded web server where you can carry out license administration tasks. When you start the license server, the default address of the license server web interface is http://localhost:5054. For more information about the license server, see http://www.reprisesoftware.com/admin/software-licensing.php.

## Setting manually which license server to use


If you want to use your own floating license server on your network and Kanzi Studio cannot find the license server automatically, you can manually set which server you want to use.

To set manually which license server to use:

1.

In a plain-text editor create a file with the lic extension that contains the word `HOST` followed by the name of your license server. For example,

```
HOST MyLicenseServer

```

2.

(Optional) To set the port for the licensing server, in the lic file you created in the previous step add a line which contains the word `ISV` followed by the name of the ISV and the port number:

```
HOST MyLicenseServer
ISV rightware port=5655

```

3.

Open Kanzi Studio and in the License Manager click Next.

If you do not have a valid Kanzi Studio license, Kanzi Studio opens the License Manager. If you already have a working license, but want to switch to a different license type, see Changing the type of Kanzi Studio license.
4.

Select License file and click Next.
5.

Click Browse, select the lic license file that you created in the first step, and click Next.

Kanzi Studio connects to the license server you set in the lic file and leases a license.

  - If the license activation is successful, click OK and start using Kanzi Studio.
  - If the license activation was not successful, the License Manager displays a message saying what went wrong.


For technical support use the Kanzi Support Portal at [http://support.rightware.com](http://support.rightware.com/). See Technical support.
