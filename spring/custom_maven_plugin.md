# Custom maven plugin:

mvn install:install-file -Dfile=../java-utils/base/target/base-0.1.jar -DgroupId=com.google.code -DartifactId=base -Dversion=0.1 -Dpackaging=jar
mvn install:install-file -Dfile=../java-utils/sqljpa/target/sqljpa-0.1.jar -DgroupId=com.google.code -DartifactId=sqljpa -Dversion=0.1 -Dpackaging=jar
