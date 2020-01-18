#! usr/bin/python3

sn_dict = {"ucl.ac.uk": {"mx": ["ucl-ac-uk.mail.protection.outlook.com"],

                         "ns": ["ns2.ja.net", "dns-ns1.ucl.ac.uk",
                                "dns-ns0.ucl.ac.uk", "ns1.cs.ucl.ac.uk"]
                         },

           "google.com": {"mx": ["alt1.aspmx.l.google.com",
                                 "aspmx.l.google.com",
                                 "alt3.aspmx.l.google.com"],

                          "ns": ["ns4.google.com internet address = 216.239.38.10",
                                 "ns2.google.com	internet address = 216.239.34.10"]
                          }
           }


def main():
    while 1:
        cmd = input(">")
        if cmd == "exit":
            break

        domain = input(">")

        for addr in sn_dict[domain][cmd]:
            print(addr)


if __name__ == "__main__":
    main()
