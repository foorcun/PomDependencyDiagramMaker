import xmltodict
# pip install xmltodict
import json
from FileService import FileService

xml_data = '''<?xml version="1.0" encoding="UTF-8"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>com.amadeus.apt.coreServices</groupId>
    <artifactId>servers</artifactId>
    <version>1.16-SNAPSHOT</version>
  </parent>
  <groupId>com.amadeus.apt.coreServices.servers</groupId>
  <artifactId>coreServicesJBoss</artifactId>
  <packaging>pom</packaging>
  <name>CoreServices JBoss server</name>
  <dependencies>
    <dependency>
      <groupId>com.amadeus.apt.frmk.pki</groupId>
      <artifactId>truststore</artifactId>
    </dependency>
    <dependency>
      <groupId>com.amadeus.apt.frmk.pki.keystores</groupId>
      <artifactId>server</artifactId>
    </dependency>
    <dependency>
      <groupId>com.amadeus.apt.coreServices.apps</groupId>
      <artifactId>coreServicesApp</artifactId>
      <version>${project.version}</version>
      <type>ear</type>
    </dependency>
    <dependency>
      <groupId>com.amadeus.apt.authentication.apps</groupId>
      <artifactId>authenticationApp-jdbc</artifactId>
      <version>2.0.3</version>
      <type>ear</type>
    </dependency>
  </dependencies>
  <profiles>
    <profile>
      <id>coreServicesJBoss_start</id>
      <build>
        <plugins>
          <plugin>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>2.9</version>
            <executions>
              <execution>
                <id>Unpack trust store/key store</id>
                <phase>prepare-package</phase>
                <goals>
                  <goal>unpack</goal>
                </goals>
                <configuration>
                  <artifactItems>
                    <artifactItem>
                      <groupId>com.amadeus.apt.frmk.pki</groupId>
                      <artifactId>truststore</artifactId>
                    </artifactItem>
                    <artifactItem>
                      <groupId>com.amadeus.apt.frmk.pki.keystores</groupId>
                      <artifactId>server</artifactId>
                    </artifactItem>
                  </artifactItems>
                  <outputDirectory>${basedir}/target/pki</outputDirectory>
                  <includes>*/.jks</includes>
                </configuration>
              </execution>
            </executions>
          </plugin>
          <plugin>
            <groupId>org.codehaus.cargo</groupId>
            <artifactId>cargo-maven2-plugin</artifactId>
            <version>1.6.1</version>
            <executions>
              <execution>
                <id>JBoss_start</id>
                <phase>verify</phase>
                <goals>
                  <goal>run</goal>
                </goals>
                <configuration>
                  <container>
                    <containerId>wildfly10x</containerId>
                    <artifactInstaller>
                      <groupId>com.amadeus.apt.application_stack</groupId>
                      <artifactId>jboss-eap</artifactId>
                      <version>7.0.2</version>
                    </artifactInstaller>
                    <systemProperties>
                      <org.jboss.as.logging.per-deployment>false</org.jboss.as.logging.per-deployment>
                    </systemProperties>
                  </container>
                  <configuration>
                    <properties>
                      <cargo.jvmargs>-Xms512M -Xmx2048M -XX:PermSize=128m -XX:MaxPermSize=512m -Xrunjdwp:transport=dt_socket,address=8787,server=y,suspend=n</cargo.jvmargs>
                    </properties>
                    <configfiles>
                      <configfile>
                        <file>${basedir}/src/main/resources/standalone.xml</file>
                        <todir>configuration</todir>
                      </configfile>
                    </configfiles>
                  </configuration>
                  <deployer>
                    <type>local</type>
                  </deployer>
                  <deployables>
                    <deployable>
                      <groupId>com.amadeus.apt.coreServices.apps</groupId>
                      <artifactId>coreServicesApp</artifactId>
                      <type>ear</type>
                    </deployable>
                    <deployable>
                      <groupId>com.amadeus.apt.authentication.apps</groupId>
                      <artifactId>authenticationApp-jdbc</artifactId>
                      <type>ear</type>
                    </deployable>
                  </deployables>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>'''


xml_data = FileService.readFile("C:\\DEV\\Mobile_projects\\coreservices\\servers\\coreServicesJBoss\\pom.xml")


def pomXmlToJson(xml_data):
    # Parse the XML
    xml_dict = xmltodict.parse(xml_data)

    # Convert to JSON
    json_data = json.dumps(xml_dict, indent=4)

    return json_data

# Print JSON
# print(pomXmlToJson(xml_data))